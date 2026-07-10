# Sprint 2: CSV Data Summary Expansion

## Problem Statement

Extend the CSV inspection tool built in Sprint 1 to provide additional data quality and descriptive summary information.

## User Requirements

The following new functionalities will be added:

1. The tool reports missing-value percentages for each variable.
2. The tool reports simple numeric summary statistics for numeric variables.
3. The tool shows each variable's type alongside its name.
4. The tool lists the available categories for categorical variables.

## Plan

Build on the Sprint 1 CSV summary tool by adding richer inspection output. The updated tool should preserve the existing row count, column count, and column name reporting while expanding the summary to include variable types, categorical categories, missing-value percentages, and basic numeric statistics.

## Tasks

- Verify the Sprint 1 behavior still works after the update.
- Keep accepting a CSV file path as input.
- Preserve the existing row count, column count, and column name output.
- Show the type of each variable alongside its name.
- For categorical variables, show the available categories.
- Calculate and display missing-value percentages for each column.
- Calculate and display simple numeric summary statistics for numeric columns.
- Update `README.md` if the tool usage or output changes.
- Confirm the final output matches the updated sprint requirements.

## Out of Scope

- Anything else.

## Definition of Done

- The Sprint 1 features still work as expected.
- The tool accepts a CSV file path.
- The tool prints the row count.
- The tool prints the column count.
- The tool prints the column names.
- The tool prints the type of each variable together with its name.
- The tool prints the available categories for categorical variables.
- The tool prints missing-value percentages for each column.
- The tool prints simple numeric summary statistics for numeric columns.
- The `README.md` explains how to run the updated tool.
