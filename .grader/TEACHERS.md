# For teachers: how assignment repositories work

Every assignment repository (`prog-lab-N`, `prog-pN`…) is created from
`template-graded-exercise` and is the Classroom 50 template of one assignment. Students get a copy
of it, including this file, so never put anything here they should not read, and never
solutions.

## What is in it

| Path | Audience | Language |
|---|---|---|
| `README.md` | Students | Spanish |
| `exercise_*.py` (one per exercise, with a header comment) | Students | Spanish header comment; file name exactly as in the sheet |
| `check.py` | Students run it; teachers maintain it | English code and messages |
| `.vscode/settings.json`, `.vscode/tasks.json` | Students' editor | English comments, Spanish task label |
| `.grader/README.md` | Students: "do not touch this folder" | Spanish |
| `.grader/assignment.toml` | Grader | English |
| `.grader/tests.json` | Grader and `check.py` | Test names in Spanish (they quote the sheet) |
| `.grader/engine.py` | Grader and `check.py` | English; a copy of the grader's, never edited here |
| `.grader/TEACHERS.md` | Teachers (this file) | English |

## Language

**Spanish for the assignment statement that students read; English for everything else.** The
full rule, with the cases that are easy to miss, is in `CONTRIBUTING.md` of `auto-grader`. In
short:

- **Spanish:** the student `README.md`, the header comment of each exercise file, test names, and
  `.grader/README.md`.
- **English:** code, identifiers, comments, configuration, messages printed by `check.py` and the
  grader, and this file.
- **Exercise file names** must match exactly what the sheet tells students to create. If you
  rename one, rename it in the sheet (its `ficheros:` front matter) and in `tests.json` too.

## Creating a new assignment

1. **Create the repository.** On GitHub, in `template-graded-exercise`: **Use this template →
   Create a new repository**. Organization `PROG-GITT-UPM`, name `prog-lab-N`, private.
2. **Starting code.** One file per exercise, with its Spanish header comment. Delete
   `exercise_01_greeting.py` if you do not use it.
3. **Tests.** Replace `.grader/tests.json` with the assignment's tests, generated from the sheet
   with the course kit script. The test files already generated for P1–P4, PF and the exams work
   as they are.
4. **Settings and README.** In `.grader/assignment.toml`, set `name` and the `protected` files
   (input data or provided modules students must not change). Adapt `README.md`.
5. **No workflows.** Do not add `.github/workflows/`: any workflow would spend Actions minutes on
   every push of every student.
6. **Validate** with the reference solution, kept outside this repository:

   ```bash
   grader validate-assignment . --solution ~/solutions/lab-N
   ```

   The untouched template must score 0 and the solution must get full marks.
7. **Mark it as a template.** In **Settings → Template repository**. Then give the classroom team
   read access (every private template needs it):

   ```bash
   gh api -X PUT orgs/PROG-GITT-UPM/teams/classroom50-<classroom>/repos/PROG-GITT-UPM/prog-lab-N -f permission=pull
   ```

8. **Create the assignment in Classroom 50** (web) with:
   - Template: this repository.
   - **Grading: Manual**, with the total points of `tests.json`.
   - **Do not use the built-in autograder** ticked.
   - Due date.
9. **Add it to the grader**, in `/etc/grader/grader.toml`, and restart it:

   ```toml
   [assignments."<classroom>/<assignment>"]
   template = "PROG-GITT-UPM/prog-lab-N"
   ```

   Add it to `watch` too if it should be graded after every push.

## Changing the tests while the assignment is running

- **Pushing to this repository is enough.** The grader reads the tests from here, not from the
  students' repositories. Submissions already graded are graded again on the next round, because
  the tests changed.
- **Students keep their own copy.** Their `.grader/` (and so `check.py`) is the copy they got when
  they accepted. If the change matters, tell them to copy the new `tests.json`.

## Changing the engine

Never edit `.grader/engine.py` here. Change it in `auto-grader` and copy it with
`grader sync-engine`.
