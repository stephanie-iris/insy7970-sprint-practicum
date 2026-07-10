# CSV Summary CLI

This project provides a small Python command-line tool that reads a CSV file and prints:

- the number of data rows
- the number of columns
- the column names with their inferred type
- missing-value percentages
- simple numeric summary statistics for numeric columns
- categories for categorical columns

## Run

Use `uv` to run the script and pass a CSV file path:

```bash
uv run python main.py data/test.csv
```

You can replace `data/test.csv` with any CSV file you want to inspect.

