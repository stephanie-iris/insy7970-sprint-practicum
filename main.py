from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path
import sys


def _clean_value(value: str) -> str:
    return value.strip()


def _is_missing(value: str) -> bool:
    return _clean_value(value) == ""


def _is_number(value: str) -> bool:
    try:
        float(_clean_value(value))
    except ValueError:
        return False
    return True


def _infer_column_type(values: list[str]) -> str:
    non_missing = [_clean_value(value) for value in values if not _is_missing(value)]
    if not non_missing:
        return "empty"
    if all(_is_number(value) for value in non_missing):
        return "numeric"
    unique_values = {value.lower() for value in non_missing}
    if len(unique_values) <= 20 and len(unique_values) <= max(1, len(non_missing) // 2):
        return "categorical"
    return "text"


def _numeric_summary(values: list[str]) -> dict[str, float] | None:
    numbers = [float(_clean_value(value)) for value in values if _is_number(value)]
    if not numbers:
        return None
    mean = sum(numbers) / len(numbers)
    variance = sum((value - mean) ** 2 for value in numbers) / len(numbers)
    return {
        "count": float(len(numbers)),
        "mean": mean,
        "min": min(numbers),
        "max": max(numbers),
        "std": math.sqrt(variance),
    }


def summarize_csv(csv_path: Path) -> tuple[int, int, list[str], list[list[str]]]:
    with csv_path.open(newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        return 0, 0, [], []

    header = rows[0]
    data_rows = rows[1:]
    columns = list(map(list, zip(*data_rows))) if data_rows else [[] for _ in header]
    if len(columns) < len(header):
        columns.extend([[] for _ in range(len(header) - len(columns))])
    return len(data_rows), len(header), header, columns


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect a CSV file and print a basic summary."
    )
    parser.add_argument("csv_path", type=Path, help="Path to the CSV file")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        row_count, column_count, column_names, columns = summarize_csv(args.csv_path)
    except FileNotFoundError:
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"Error: could not read {args.csv_path}: {exc}", file=sys.stderr)
        return 1

    print(f"Rows: {row_count}")
    print(f"Columns: {column_count}")
    print("Columns:")
    for name, values in zip(column_names, columns, strict=False):
        column_type = _infer_column_type(values)
        print(f"- {name} ({column_type})")
        missing_count = sum(1 for value in values if _is_missing(value))
        missing_percentage = (missing_count / row_count * 100) if row_count else 0.0
        print(f"  Missing values: {missing_count} ({missing_percentage:.1f}%)")

        if column_type == "numeric":
            summary = _numeric_summary(values)
            if summary:
                print("  Numeric summary:")
                print(f"    Count: {int(summary['count'])}")
                print(f"    Mean: {summary['mean']:.2f}")
                print(f"    Min: {summary['min']:.2f}")
                print(f"    Max: {summary['max']:.2f}")
                print(f"    Std dev: {summary['std']:.2f}")
        elif column_type == "categorical":
            categories = []
            seen = set()
            for value in values:
                cleaned = _clean_value(value)
                if not cleaned:
                    continue
                key = cleaned.lower()
                if key in seen:
                    continue
                seen.add(key)
                categories.append(cleaned)
            print("  Categories:")
            for category in categories:
                print(f"    - {category}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
