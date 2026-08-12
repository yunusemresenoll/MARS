"""Small, dependency-free readers for archived PDS3 fixed binary products."""

from __future__ import annotations

from array import array
from dataclasses import dataclass
from pathlib import Path
import sys


@dataclass(frozen=True)
class Int16GridSummary:
    cells: int
    minimum: int
    minimum_row: int
    minimum_column: int
    maximum: int
    maximum_row: int
    maximum_column: int
    zero_cells: int


def summarize_msb_int16_grid(
    path: Path,
    *,
    lines: int,
    samples_per_line: int,
) -> Int16GridSummary:
    expected_cells = lines * samples_per_line
    values = array("h")
    with path.open("rb") as handle:
        values.fromfile(handle, expected_cells)
        if handle.read(1):
            raise ValueError(f"Beklenmeyen ek raster baytı: {path}")
    if len(values) != expected_cells:
        raise ValueError(
            f"Eksik raster: {path} ({len(values)} != {expected_cells} hücre)"
        )
    if sys.byteorder == "little":
        values.byteswap()

    minimum = min(values)
    maximum = max(values)
    minimum_index = values.index(minimum)
    maximum_index = values.index(maximum)
    return Int16GridSummary(
        cells=expected_cells,
        minimum=minimum,
        minimum_row=minimum_index // samples_per_line,
        minimum_column=minimum_index % samples_per_line,
        maximum=maximum,
        maximum_row=maximum_index // samples_per_line,
        maximum_column=maximum_index % samples_per_line,
        zero_cells=values.count(0),
    )


def simple_cylindrical_cell_center(
    row: int,
    column: int,
    *,
    pixels_per_degree: float,
    north_edge_deg: float = 90.0,
    west_edge_deg: float = 0.0,
) -> tuple[float, float]:
    latitude = north_edge_deg - (row + 0.5) / pixels_per_degree
    longitude_east = west_edge_deg + (column + 0.5) / pixels_per_degree
    return latitude, longitude_east
