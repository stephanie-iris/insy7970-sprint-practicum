from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys


def summarize_csv(csv_path: Path) -> tuple[int, int, list[str]]:
    with csv_path.open(newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        return 0, 0, []

    header = rows[0]
    data_rows = rows[1:]
    return len(data_rows), len(header), header


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
        row_count, column_count, column_names = summarize_csv(args.csv_path)
    except FileNotFoundError:
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"Error: could not read {args.csv_path}: {exc}", file=sys.stderr)
        return 1

    print(f"Rows: {row_count}")
    print(f"Columns: {column_count}")
    print("Column names:")
    for name in column_names:
        print(f"- {name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
