# Practicum 3 Submission

**Operating system:** *Windows* 

**Terminal used:** *Git Bash*

**Codex tool used:** *GPT 5.5 Medium*

**GitHub repository URL:** *https://github.com/stephanie-iris/insy7970-sprint-practicum*

## Setup notes

- **project folder path from pwd:**

*/c/Users/fanei/insy7970/insy7970-sprint-practicum*

- **whether uv run main.py worked at the starting point, or the exact error if it did not run:**

*It ran successfully.*

- **1–2 sentences explaining what files `uv init` created:**

*`uv init` created the project configuration files: `pyproject.toml` (project metadata and dependencies), `.python-version` (Python version), and `README.md` (project documentation template). After creating the virtual environment and installing dependencies, it also generated the `.venv/` directory and the `uv.lock` file to ensure reproducible dependency versions.*

- **confirmation that .gitignore excludes .venv/ and cache folders:**

*Confirmed. The .gitignore excludes .venv/ and Python cache folders (e.g., __pycache__/).*

## Sprint 1 summary

- **The Codex prompt you used before it edited `sprint1.md`:**

*Please revise the Definition of Done so that every item maps directly to one of the user requirements. Avoid adding completion criteria that are not already part of the sprint goals.*

- **2–4 sentences describing how you defined the user requirements:**

*I focused on the minimum functionality needed for a first working version of the tool. I wrote the requirements from the user's perspective and kept them specific and easy to verify.*

- **One thing Codex added to the spec that helped you think more clearly:**

*Codex suggested documenting the run instructions in the README.md, which clarified where user documentation should live*

- **Are you able to follow what it is doing? Did you have to give permission for any steps? Did you stop it to ask a question or redirect it?**

*Yes. I was able to follow what Codex was doing throughout the process. I had to approve changes to `main.py` and `README.md`, as well as allow it to inspect the code. I did not need to stop it or redirect it.*

- **The command you used to run the Sprint 1 implementation:**

uv run python main.py data/test.csv

- **The result of that run, summarized with key output or exact error:**

Rows: 262

Columns: 19

Column names:
- request_id
- external_ticket
- submitted_at
- closed_at
- neighborhood
- station_id
- asset_tag
- service_type
- status
- priority
- source
- estimated_cost_usd
- hours_open
- latitude
- longitude
- assigned_team
- requester_type
- reported_by
- notes

- **The name of one file you inspected and what you looked for:**

*I inspected `main.py` to understand what had been implemented and `README.md` to review the instructions for running the tool.*

- **3-5 sentences explaining whether the Sprint 1 definition of done was met and how you confirmed that:**

*The Sprint 1 definition of done was met. I confirmed this by running the tool and verifying that its output matched the expected behavior. I also checked that all items in the definition of done were satisfied and that the `README.md` included the required run instructions.*

- **Sprint 1 commit message or short commit hash**

$ git log --oneline
8ffd551 (HEAD -> main) Implement Sprint 1

- **Confirmation that Sprint 1 files are visible on GitHub, or the exact push/authentication blocker:**

*Confirmed. The Sprint 1 files were successfully pushed and are visible on GitHub.*

## Sprint 2 summary

## Workflow reflection

## Practicum feedback

## Unresolved question
