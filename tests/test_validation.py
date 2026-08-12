import json
import struct
import tempfile
import unittest
import zipfile
from pathlib import Path

from mars_foundation.validation import (
    ProvenanceError,
    count_binary_cells,
    count_fixed_records,
    count_pds_array_elements,
    count_pds_table_records,
    count_stream_rows,
    count_zip_binary_cells,
    count_zip_dbf_records,
    count_zip_member_lines,
    load_source_catalog,
    require_zip_members,
    validate_value_record,
)
from mars_foundation.pds3 import (
    simple_cylindrical_cell_center,
    summarize_msb_int16_grid,
)


class ProvenanceTests(unittest.TestCase):
    def test_msb_int16_grid_summary_and_coordinates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "grid.img"
            path.write_bytes(struct.pack(">hhhhhh", 4, -7, 0, 2, 9, 1))
            summary = summarize_msb_int16_grid(
                path,
                lines=2,
                samples_per_line=3,
            )
            self.assertEqual((summary.minimum, summary.minimum_row), (-7, 0))
            self.assertEqual(
                (summary.maximum, summary.maximum_row, summary.maximum_column),
                (9, 1, 1),
            )
            self.assertEqual(summary.zero_cells, 1)
            self.assertEqual(
                simple_cylindrical_cell_center(
                    0,
                    0,
                    pixels_per_degree=16,
                ),
                (89.96875, 0.03125),
            )

    def test_fixed_length_records_are_counted_from_file_size(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixed.bin"
            path.write_bytes(b"\x00" * 366)
            self.assertEqual(count_fixed_records(path, 122), 3)

    def test_binary_cells_are_counted_from_sample_bits(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "grid.img"
            path.write_bytes(b"\x00" * 20)
            self.assertEqual(count_binary_cells(path, 16), 10)

    def test_stream_rows_are_counted_after_header_offset(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stream.tab"
            path.write_bytes(b"HEADER" + b"\x00" * 36)
            self.assertEqual(count_stream_rows(path, 6, 12), 3)

    def test_pds_array_elements_are_read_from_named_array(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "product.xml"
            path.write_text(
                """<?xml version="1.0"?>
<Product_Observational xmlns="http://pds.nasa.gov/pds4/pds/v1">
  <File_Area_Observational>
    <Array>
      <local_identifier>epoch</local_identifier>
      <Axis_Array><axis_name>index</axis_name><elements>21600</elements></Axis_Array>
    </Array>
  </File_Area_Observational>
</Product_Observational>
""",
                encoding="utf-8",
            )
            self.assertEqual(count_pds_array_elements(path, "epoch"), 21600)

    def test_pds_multidimensional_array_elements_are_multiplied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cube.xml"
            path.write_text(
                """<?xml version="1.0"?>
<Product_Observational xmlns="http://pds.nasa.gov/pds4/pds/v1">
  <File_Area_Observational>
    <Array_3D_Spectrum>
      <local_identifier>radiance</local_identifier>
      <Axis_Array><axis_name>Time</axis_name><elements>33</elements></Axis_Array>
      <Axis_Array><axis_name>Line</axis_name><elements>7</elements></Axis_Array>
      <Axis_Array><axis_name>Sample</axis_name><elements>512</elements></Axis_Array>
    </Array_3D_Spectrum>
  </File_Area_Observational>
</Product_Observational>
""",
                encoding="utf-8",
            )
            self.assertEqual(
                count_pds_array_elements(path, "radiance"),
                33 * 7 * 512,
            )

    def test_pds_table_records_are_read_from_named_table(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "table.xml"
            path.write_text(
                """<?xml version="1.0"?>
<Product_Observational xmlns="http://pds.nasa.gov/pds4/pds/v1">
  <File_Area_Observational>
    <Table_Binary>
      <local_identifier>density</local_identifier>
      <records>14</records>
    </Table_Binary>
  </File_Area_Observational>
</Product_Observational>
""",
                encoding="utf-8",
            )
            self.assertEqual(count_pds_table_records(path, "density"), 14)

    def test_zip_text_records_are_counted_across_matching_members(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "spectra.zip"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("data/a.tab", "1\n2\n")
                archive.writestr("data/b.tab", "3\n")
                archive.writestr("data/ignore.lbl", "LABEL\n")
            self.assertEqual(count_zip_member_lines(path, "data/*.tab"), 3)

    def test_dbf_record_count_is_read_from_zip_header(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "vectors.zip"
            header = bytearray(32)
            header[4:8] = struct.pack("<I", 1311)
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("layers/geology.dbf", header)
            self.assertEqual(
                count_zip_dbf_records(path, "layers/geology.dbf"),
                1311,
            )

    def test_zip_binary_cells_use_uncompressed_member_size(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "rasters.zip"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("data/grid.img", b"\x00" * 40)
            self.assertEqual(
                count_zip_binary_cells(path, "data/grid.img", 16),
                20,
            )

    def test_required_zip_member_pattern_must_match(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "archive.zip"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("data/product.lbl", "LABEL\n")
            self.assertEqual(require_zip_members(path, "data/*.lbl"), 1)
            with self.assertRaisesRegex(ProvenanceError, "eşleşen üye yok"):
                require_zip_members(path, "data/*.xml")

    def test_empty_source_catalog_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sources.json"
            path.write_text(
                json.dumps({"catalog_version": "1.0.0", "sources": []}),
                encoding="utf-8",
            )
            self.assertEqual(load_source_catalog(path), {})

    def test_value_without_registered_source_is_rejected(self) -> None:
        record = {
            "record_id": "mars.example.1",
            "property_id": "atmosphere.pressure",
            "status": "MEASURED",
            "value": 0,
            "unit": "Pa",
            "location": {"scope": "POINT"},
            "time": {"temporal_scope": "INSTANT"},
            "uncertainty": {"kind": "NOT_AVAILABLE"},
            "source_id": "missing.source",
            "source_locator": "Table 1",
        }
        with self.assertRaisesRegex(ProvenanceError, "Bilinmeyen source_id"):
            validate_value_record(record, {})

    def test_value_with_registered_source_is_accepted(self) -> None:
        record = {
            "record_id": "mars.example.1",
            "property_id": "atmosphere.pressure",
            "status": "MEASURED",
            "value": 0,
            "unit": "Pa",
            "location": {"scope": "POINT"},
            "time": {"temporal_scope": "INSTANT"},
            "uncertainty": {"kind": "NOT_AVAILABLE"},
            "source_id": "nasa.example",
            "source_locator": "Table 1",
        }
        validate_value_record(record, {"nasa.example": {}})

    def test_value_with_unknown_property_is_rejected(self) -> None:
        record = {
            "record_id": "mars.example.1",
            "property_id": "atmosphere.pressure",
            "status": "MEASURED",
            "value": 0,
            "unit": "Pa",
            "location": {"scope": "POINT"},
            "time": {"temporal_scope": "INSTANT"},
            "uncertainty": {"kind": "NOT_AVAILABLE"},
            "source_id": "nasa.example",
            "source_locator": "Table 1",
        }
        with self.assertRaisesRegex(ProvenanceError, "Bilinmeyen property_id"):
            validate_value_record(record, {"nasa.example": {}}, {})


if __name__ == "__main__":
    unittest.main()
