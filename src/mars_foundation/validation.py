"""Provenance validation for MARS source and value records."""

from __future__ import annotations

import hashlib
import fnmatch
import json
import struct
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RESOURCES_ROOT = PROJECT_ROOT / "resources"
SOURCE_CATALOG = RESOURCES_ROOT / "catalog" / "sources.json"
PROPERTY_REGISTRY = PROJECT_ROOT / "data" / "registry" / "properties.json"
FOUNDATION_VALUES = PROJECT_ROOT / "data" / "values" / "foundation.json"

SOURCE_REQUIRED_FIELDS = {
    "source_id",
    "title",
    "publisher",
    "url",
    "retrieved_at",
    "license",
    "archived",
    "archive_files",
    "citation",
}

VALUE_REQUIRED_FIELDS = {
    "record_id",
    "property_id",
    "status",
    "value",
    "unit",
    "location",
    "time",
    "uncertainty",
    "source_id",
    "source_locator",
}

VALID_STATUSES = {"MEASURED", "DERIVED", "MODELLED", "UNKNOWN"}

PROPERTY_REQUIRED_FIELDS = {
    "property_id",
    "domain",
    "name_en",
    "name_tr",
    "definition",
    "canonical_unit",
    "value_kind",
    "spatial_scope",
    "temporal_behavior",
    "vertical_behavior",
    "allowed_statuses",
    "definition_sources",
}


class ProvenanceError(ValueError):
    """Raised when a source or value breaks the provenance contract."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def count_binary_lines(path: Path) -> int:
    count = 0
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            count += block.count(b"\n")
    return count


def count_fixed_records(path: Path, record_bytes: int) -> int:
    if record_bytes < 1:
        raise ProvenanceError("record_bytes pozitif bir tamsayı olmalıdır")
    size = path.stat().st_size
    if size % record_bytes:
        raise ProvenanceError(
            f"Dosya boyutu sabit kayıt uzunluğuna bölünmüyor: "
            f"{path.name} ({size} / {record_bytes})"
        )
    return size // record_bytes


def count_stream_rows(
    path: Path,
    data_offset_bytes: int,
    record_bytes: int,
) -> int:
    if data_offset_bytes < 0:
        raise ProvenanceError("data_offset_bytes negatif olamaz")
    if record_bytes < 1:
        raise ProvenanceError("record_bytes pozitif bir tamsayı olmalıdır")
    data_bytes = path.stat().st_size - data_offset_bytes
    if data_bytes < 0 or data_bytes % record_bytes:
        raise ProvenanceError(
            f"Akış tablosu boyutu kayıt yapısıyla uyuşmuyor: {path.name} "
            f"(({path.stat().st_size} - {data_offset_bytes}) / {record_bytes})"
        )
    return data_bytes // record_bytes


def count_binary_cells(path: Path, sample_bits: int) -> int:
    if sample_bits < 1:
        raise ProvenanceError("sample_bits pozitif bir tamsayı olmalıdır")
    total_bits = path.stat().st_size * 8
    if total_bits % sample_bits:
        raise ProvenanceError(
            f"Dosya boyutu örnek bit sayısına bölünmüyor: "
            f"{path.name} ({total_bits} / {sample_bits})"
        )
    return total_bits // sample_bits


def count_pds_array_elements(label_path: Path, local_identifier: str) -> int:
    """Multiply the axis lengths of a named PDS4 Array from its label."""
    try:
        root = ET.parse(label_path).getroot()
    except ET.ParseError as error:
        raise ProvenanceError(f"Geçersiz PDS4 XML etiketi: {label_path.name}") from error

    for array in root.iter():
        if not array.tag.rsplit("}", 1)[-1].startswith("Array"):
            continue
        identifier = next(
            (
                child.text
                for child in array
                if child.tag.rsplit("}", 1)[-1] == "local_identifier"
            ),
            None,
        )
        if identifier != local_identifier:
            continue
        axis_lengths: list[int] = []
        for descendant in array.iter():
            if descendant.tag.rsplit("}", 1)[-1] != "Axis_Array":
                continue
            elements = next(
                (
                    child.text
                    for child in descendant
                    if child.tag.rsplit("}", 1)[-1] == "elements"
                ),
                None,
            )
            if elements is not None:
                try:
                    value = int(elements)
                except ValueError as error:
                    raise ProvenanceError(
                        f"PDS4 dizi eleman sayısı tamsayı değil: {label_path.name}"
                    ) from error
                if value < 1:
                    raise ProvenanceError(
                        f"PDS4 dizi eleman sayısı pozitif değil: {label_path.name}"
                    )
                axis_lengths.append(value)
        if axis_lengths:
            total = 1
            for value in axis_lengths:
                total *= value
            return total
        raise ProvenanceError(
            f"PDS4 dizisinde Axis_Array/elements yok: "
            f"{label_path.name}:{local_identifier}"
        )
    raise ProvenanceError(
        f"PDS4 etiketinde dizi bulunamadı: {label_path.name}:{local_identifier}"
    )


def count_pds_table_records(label_path: Path, local_identifier: str) -> int:
    """Read the record count of a named PDS4 table from its label."""
    try:
        root = ET.parse(label_path).getroot()
    except ET.ParseError as error:
        raise ProvenanceError(f"Geçersiz PDS4 XML etiketi: {label_path.name}") from error

    for table in root.iter():
        if not table.tag.rsplit("}", 1)[-1].startswith("Table_"):
            continue
        identifier = next(
            (
                child.text
                for child in table
                if child.tag.rsplit("}", 1)[-1] == "local_identifier"
            ),
            None,
        )
        if identifier != local_identifier:
            continue
        records = next(
            (
                child.text
                for child in table
                if child.tag.rsplit("}", 1)[-1] == "records"
            ),
            None,
        )
        if records is None:
            raise ProvenanceError(
                f"PDS4 tablosunda records yok: {label_path.name}:{local_identifier}"
            )
        try:
            value = int(records)
        except ValueError as error:
            raise ProvenanceError(
                f"PDS4 tablo kayıt sayısı tamsayı değil: {label_path.name}"
            ) from error
        if value < 1:
            raise ProvenanceError(
                f"PDS4 tablo kayıt sayısı pozitif değil: {label_path.name}"
            )
        return value
    raise ProvenanceError(
        f"PDS4 etiketinde tablo bulunamadı: {label_path.name}:{local_identifier}"
    )


def count_zip_member_lines(path: Path, member_pattern: str) -> int:
    count = 0
    matched = 0
    with zipfile.ZipFile(path) as archive:
        for member in archive.namelist():
            if not fnmatch.fnmatch(member, member_pattern):
                continue
            matched += 1
            with archive.open(member) as handle:
                for block in iter(lambda: handle.read(1024 * 1024), b""):
                    count += block.count(b"\n")
    if matched == 0:
        raise ProvenanceError(
            f"ZIP içinde desenle eşleşen üye yok: {path.name}:{member_pattern}"
        )
    return count


def require_zip_members(path: Path, member_pattern: str) -> int:
    with zipfile.ZipFile(path) as archive:
        matched = sum(
            1 for member in archive.namelist()
            if fnmatch.fnmatch(member, member_pattern)
        )
    if matched == 0:
        raise ProvenanceError(
            f"ZIP içinde desenle eşleşen üye yok: {path.name}:{member_pattern}"
        )
    return matched


def count_zip_dbf_records(path: Path, member: str) -> int:
    with zipfile.ZipFile(path) as archive:
        try:
            header = archive.read(member)[:32]
        except KeyError as error:
            raise ProvenanceError(
                f"ZIP içinde DBF üyesi bulunamadı: {path.name}:{member}"
            ) from error
    if len(header) < 8:
        raise ProvenanceError(f"Geçersiz DBF başlığı: {path.name}:{member}")
    return struct.unpack("<I", header[4:8])[0]


def count_zip_binary_cells(path: Path, member: str, sample_bits: int) -> int:
    if sample_bits < 1:
        raise ProvenanceError("sample_bits pozitif bir tamsayı olmalıdır")
    with zipfile.ZipFile(path) as archive:
        try:
            member_bytes = archive.getinfo(member).file_size
        except KeyError as error:
            raise ProvenanceError(
                f"ZIP içinde ikili üye bulunamadı: {path.name}:{member}"
            ) from error
    total_bits = member_bytes * 8
    if total_bits % sample_bits:
        raise ProvenanceError(
            f"ZIP üye boyutu örnek bit sayısına bölünmüyor: "
            f"{path.name}:{member} ({total_bits} / {sample_bits})"
        )
    return total_bits // sample_bits


def load_source_catalog(path: Path = SOURCE_CATALOG) -> dict[str, dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    sources = payload.get("sources")
    if not isinstance(sources, list):
        raise ProvenanceError("sources.json içindeki 'sources' bir liste olmalıdır")

    catalog: dict[str, dict[str, Any]] = {}
    for source in sources:
        validate_source_record(source)
        source_id = source["source_id"]
        if source_id in catalog:
            raise ProvenanceError(f"Tekrarlanan source_id: {source_id}")
        catalog[source_id] = source
    return catalog


def validate_source_record(source: dict[str, Any]) -> None:
    missing = SOURCE_REQUIRED_FIELDS - source.keys()
    if missing:
        raise ProvenanceError(f"Kaynak alanları eksik: {sorted(missing)}")

    archived = source["archived"]
    files = source["archive_files"]
    if not isinstance(archived, bool):
        raise ProvenanceError("'archived' boolean olmalıdır")
    if not isinstance(files, list):
        raise ProvenanceError("'archive_files' liste olmalıdır")
    if archived and not files:
        raise ProvenanceError("Arşivlenmiş kaynak en az bir yerel dosya içermelidir")
    if not archived and not source.get("archive_exception"):
        raise ProvenanceError("Arşivlenemeyen kaynak için archive_exception zorunludur")

    for item in files:
        relative_path = Path(item["path"])
        if relative_path.is_absolute() or ".." in relative_path.parts:
            raise ProvenanceError(f"Güvensiz kaynak yolu: {relative_path}")
        file_path = RESOURCES_ROOT / relative_path
        if not file_path.is_file():
            raise ProvenanceError(f"Kaynak dosyası bulunamadı: {relative_path}")
        actual_size = file_path.stat().st_size
        if actual_size != item["bytes"]:
            raise ProvenanceError(f"Dosya boyutu uyuşmuyor: {relative_path}")
        actual_hash = sha256_file(file_path)
        if actual_hash != item["sha256"]:
            raise ProvenanceError(f"SHA-256 uyuşmuyor: {relative_path}")


def validate_value_record(
    record: dict[str, Any],
    source_catalog: dict[str, dict[str, Any]],
    property_registry: dict[str, dict[str, Any]] | None = None,
) -> None:
    missing = VALUE_REQUIRED_FIELDS - record.keys()
    if missing:
        raise ProvenanceError(f"Değer alanları eksik: {sorted(missing)}")
    if record["status"] not in VALID_STATUSES:
        raise ProvenanceError(f"Geçersiz veri durumu: {record['status']}")
    if record["source_id"] not in source_catalog:
        raise ProvenanceError(f"Bilinmeyen source_id: {record['source_id']}")
    if property_registry is not None and record["property_id"] not in property_registry:
        raise ProvenanceError(f"Bilinmeyen property_id: {record['property_id']}")
    if not str(record["source_locator"]).strip():
        raise ProvenanceError("Kaynak içindeki kesin konum source_locator ile verilmelidir")


def load_property_registry(
    source_catalog: dict[str, dict[str, Any]],
    path: Path = PROPERTY_REGISTRY,
) -> dict[str, dict[str, Any]]:
    registry: dict[str, dict[str, Any]] = {}
    paths = [path]
    if path == PROPERTY_REGISTRY:
        paths.extend(sorted(path.parent.glob("*-properties.json")))

    for registry_path in paths:
        payload = json.loads(registry_path.read_text(encoding="utf-8"))
        properties = payload.get("properties")
        if not isinstance(properties, list):
            raise ProvenanceError(
                f"{registry_path.name} içindeki 'properties' bir liste olmalıdır"
            )
        if payload.get("property_count") != len(properties):
            raise ProvenanceError(
                f"{registry_path.name}: property_count gerçek sayıyla uyuşmuyor"
            )

        for item in properties:
            missing = PROPERTY_REQUIRED_FIELDS - item.keys()
            if missing:
                raise ProvenanceError(f"Özellik alanları eksik: {sorted(missing)}")
            property_id = item["property_id"]
            if property_id in registry:
                raise ProvenanceError(f"Tekrarlanan property_id: {property_id}")
            if not item["definition_sources"]:
                raise ProvenanceError(f"Tanım kaynağı olmayan özellik: {property_id}")
            for reference in item["definition_sources"]:
                if reference["source_id"] not in source_catalog:
                    raise ProvenanceError(
                        f"{property_id} bilinmeyen tanım kaynağı kullanıyor: "
                        f"{reference['source_id']}"
                    )
                if not str(reference["locator"]).strip():
                    raise ProvenanceError(f"{property_id} için kaynak konumu boş")
            registry[property_id] = item
    return registry


def validate_value_dataset(
    source_catalog: dict[str, dict[str, Any]],
    property_registry: dict[str, dict[str, Any]],
    path: Path = FOUNDATION_VALUES,
) -> int:
    payload = json.loads(path.read_text(encoding="utf-8"))
    records = payload.get("records")
    if not isinstance(records, list):
        raise ProvenanceError("Değer veri kümesindeki 'records' bir liste olmalıdır")
    if payload.get("record_count") != len(records):
        raise ProvenanceError("record_count gerçek kayıt sayısıyla uyuşmuyor")
    seen: set[str] = set()
    for record in records:
        if record.get("record_id") in seen:
            raise ProvenanceError(f"Tekrarlanan record_id: {record['record_id']}")
        validate_value_record(record, source_catalog, property_registry)
        property_definition = property_registry[record["property_id"]]
        if record["status"] not in property_definition["allowed_statuses"]:
            raise ProvenanceError(
                f"{record['property_id']} için izin verilmeyen durum: {record['status']}"
            )
        if record["unit"] != property_definition["canonical_unit"]:
            raise ProvenanceError(
                f"{record['property_id']} birimi kanonik birimle uyuşmuyor: "
                f"{record['unit']} != {property_definition['canonical_unit']}"
            )
        seen.add(record["record_id"])
    return len(records)


def validate_all_value_datasets(
    source_catalog: dict[str, dict[str, Any]],
    property_registry: dict[str, dict[str, Any]],
) -> int:
    paths = sorted((PROJECT_ROOT / "data" / "values").glob("*.json"))
    if not paths:
        raise ProvenanceError("Hiç değer veri kümesi bulunamadı")
    return sum(
        validate_value_dataset(source_catalog, property_registry, path)
        for path in paths
    )


def validate_archived_datasets(
    source_catalog: dict[str, dict[str, Any]],
    property_registry: dict[str, dict[str, Any]],
) -> tuple[int, int]:
    paths = sorted((PROJECT_ROOT / "data" / "datasets").glob("*.json"))
    product_count = 0
    row_count = 0
    for path in paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        source_id = payload.get("source_id")
        if source_id not in source_catalog:
            raise ProvenanceError(f"{path.name}: bilinmeyen source_id: {source_id}")
        products = payload.get("products")
        if not isinstance(products, list) or not products:
            raise ProvenanceError(f"{path.name}: products boş veya liste değil")
        for product in products:
            property_id = product.get("property_id")
            if property_id not in property_registry:
                raise ProvenanceError(
                    f"{path.name}: bilinmeyen property_id: {property_id}"
                )
            for key in ("data_path", "label_path"):
                product_path = PROJECT_ROOT / product[key]
                if not product_path.is_file():
                    raise ProvenanceError(
                        f"{path.name}: ürün dosyası bulunamadı: {product[key]}"
                    )
            records = product.get("records")
            if not isinstance(records, int) or records < 1:
                raise ProvenanceError(f"{path.name}: geçersiz records değeri")
            data_path = PROJECT_ROOT / product["data_path"]
            count_method = product.get("record_count_method", "TEXT_LINES")
            if count_method == "TEXT_LINES":
                actual_records = count_binary_lines(data_path)
            elif count_method == "ZIP_TEXT_LINES":
                member_pattern = product.get("data_member_pattern")
                if not member_pattern:
                    raise ProvenanceError(
                        f"{path.name}: ZIP_TEXT_LINES için data_member_pattern gerekli"
                    )
                actual_records = count_zip_member_lines(data_path, member_pattern)
            elif count_method == "ZIP_DBF_RECORDS":
                member = product.get("data_member")
                if not member:
                    raise ProvenanceError(
                        f"{path.name}: ZIP_DBF_RECORDS için data_member gerekli"
                    )
                actual_records = count_zip_dbf_records(data_path, member)
            elif count_method == "ZIP_BINARY_CELLS":
                member = product.get("data_member")
                sample_bits = product.get("sample_bits")
                if not member or not isinstance(sample_bits, int):
                    raise ProvenanceError(
                        f"{path.name}: ZIP_BINARY_CELLS için data_member ve "
                        "sample_bits gerekli"
                    )
                actual_records = count_zip_binary_cells(
                    data_path,
                    member,
                    sample_bits,
                )
            elif count_method == "FIXED_BYTES":
                record_bytes = product.get("record_bytes")
                if not isinstance(record_bytes, int):
                    raise ProvenanceError(
                        f"{path.name}: FIXED_BYTES için record_bytes gerekli"
                    )
                actual_records = count_fixed_records(data_path, record_bytes)
            elif count_method == "PDS_STREAM_ROWS":
                record_bytes = product.get("record_bytes")
                data_offset_bytes = product.get("data_offset_bytes")
                if (
                    not isinstance(record_bytes, int)
                    or not isinstance(data_offset_bytes, int)
                ):
                    raise ProvenanceError(
                        f"{path.name}: PDS_STREAM_ROWS için record_bytes ve "
                        "data_offset_bytes gerekli"
                    )
                actual_records = count_stream_rows(
                    data_path,
                    data_offset_bytes,
                    record_bytes,
                )
            elif count_method == "BINARY_CELLS":
                sample_bits = product.get("sample_bits")
                if not isinstance(sample_bits, int):
                    raise ProvenanceError(
                        f"{path.name}: BINARY_CELLS için sample_bits gerekli"
                    )
                actual_records = count_binary_cells(data_path, sample_bits)
            elif count_method == "PDS_ARRAY_ELEMENTS":
                label_array_id = product.get("label_array_id")
                if not label_array_id:
                    raise ProvenanceError(
                        f"{path.name}: PDS_ARRAY_ELEMENTS için "
                        "label_array_id gerekli"
                    )
                actual_records = count_pds_array_elements(
                    PROJECT_ROOT / product["label_path"],
                    label_array_id,
                )
            elif count_method == "PDS_TABLE_RECORDS":
                label_array_id = product.get("label_array_id")
                if not label_array_id:
                    raise ProvenanceError(
                        f"{path.name}: PDS_TABLE_RECORDS için "
                        "label_array_id gerekli"
                    )
                actual_records = count_pds_table_records(
                    PROJECT_ROOT / product["label_path"],
                    label_array_id,
                )
            else:
                raise ProvenanceError(
                    f"{path.name}: bilinmeyen record_count_method: {count_method}"
                )
            label_member_pattern = product.get("label_member_pattern")
            if label_member_pattern:
                require_zip_members(
                    PROJECT_ROOT / product["label_path"],
                    label_member_pattern,
                )
            geometry_member = product.get("structure", {}).get("geometry_member")
            if geometry_member:
                require_zip_members(data_path, geometry_member)
            if actual_records != records:
                raise ProvenanceError(
                    f"{path.name}: {product['product_id']} satır sayısı uyuşmuyor: "
                    f"{actual_records} != {records}"
                )
            product_count += 1
            row_count += records
    return product_count, row_count


def main() -> int:
    catalog = load_source_catalog()
    registry = load_property_registry(catalog)
    record_count = validate_all_value_datasets(catalog, registry)
    product_count, row_count = validate_archived_datasets(catalog, registry)
    print(
        "MARS doğrulaması başarılı: "
        f"{len(catalog)} kaynak, {len(registry)} özellik, {record_count} değer, "
        f"{product_count} kaynak veri ürünü, {row_count} kaynak kaydı"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
