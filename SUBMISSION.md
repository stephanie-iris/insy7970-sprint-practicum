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
`8ffd551` *(HEAD -> main) Implement Sprint 1*

- **Confirmation that Sprint 1 files are visible on GitHub, or the exact push/authentication blocker:**

*Confirmed. The Sprint 1 files were successfully pushed and are visible on GitHub.*

## Sprint 2 summary

- **The Sprint 2 theme:**

*Extend the CSV inspection tool built in Sprint 1 to provide additional data quality and descriptive summary information.*

- **The Codex prompt you used before it edited `sprint2.md`:**

*This is a new sprint specification that builds on the tool created in Sprint 1, not an expansion of the Sprint 1 document. Avoid repeating functionality that has already been implemented, but include verification that the existing Sprint 1 features continue to work. Do not edit code yet.*

- **A description of the process you used to check the implementation and your findings:**

*I inspected the changes in `main.py` using `git diff` and reviewed the updated `README.md` with `bat`. I then ran the tool using `uv` and verified that the output matched the Sprint 2 requirements.*

- **The Sprint 2 commit message or short commit hash:**

`a8e71a8` *(HEAD -> main) Implement Sprint 2*

- **Confirmation that Sprint 2 was pushed to GitHub, or the exact push blocker:**

*Confirmed. The Sprint 2 changes were successfully pushed and are visible on GitHub.*

- **3–5 sentences explaining whether the Sprint 2 definition of done was met:**

*The Sprint 2 definition of done was met. I verified that all required changes were implemented and that the new functionality worked as expected. I also confirmed that the features implemented in Sprint 1 continued to work correctly after the Sprint 2 changes.*

## Workflow reflection

- **Connection to Lectures 03A–04B**

*This practicum provided hands-on experience with the main topics covered in Lectures 03A–04B. It reinforced the use of Git for version control, the importance of writing clear specifications before coding, the benefits of managing projects with `uv`, and the value of organizing development into small, well-defined sprints.*

- **How did starting with a problem statement and user requirements affect Codex's work?**

*Starting with a clear problem statement and user requirements made Codex's work much more efficient. Having a standardized specification helped me remember to include important information so its responses matched what I wanted. It also created a documented history of the project requirements, instead of leaving those decisions only in the chat conversation.*

- **What did Codex add to the sprint specs that you would not have written on your own?**

*Codex helped me identify details that I had forgotten or was unsure about. Its additions made the sprint specifications more complete and taught me how to better organize plans, tasks, and completion criteria.*

- **How did `uv` help with running or managing the project?**

*I normally use Conda, but I liked `uv` much more. It is simple to use and automatically handles tasks that I would otherwise have to manage myself, such as activating the correct environment when working in the project directory. This reduces the chance of human error and makes the workflow smoother.*

- **What would you do differently in a third sprint?**

*After reviewing the Sprint 2 results, I noticed that some fields that should be treated as numeric values were interpreted as text. I also found that some columns, such as latitude and longitude, were included in the summary even though they should not be analyzed that way. In a third sprint, I would focus on addressing these issues to improve the quality and usefulness of the tool's output.*

## Practicum feedback

- **What part of this practicum was most useful?**

*I liked the practicum format because it let us apply the concepts ourselves in a small project. It felt like working on a real project, but in a low-pressure environment where the focus was on learning and practicing.*

- **What part was most confusing, frustrating, or in need of clearer instructions?**

*The most confusing part was understanding exactly what information was expected in `SUBMISSION.md`. I hope I included everything that was required.*

## Unresolved question
