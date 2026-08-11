# LPIC-1 Quality Check

This is an internal repository-quality rubric, not an official LPI endorsement
and not a guarantee of an exam result. A score of 10 means the stated check is
fully satisfied by the current repository revision.

| Area | Score | Evidence |
|---|---:|---|
| Official scope | 10/10 | All 42 active version 5.0 objectives for `101-500` and `102-500` are mapped in `OBJECTIVES.md` and have matching chapter headings. |
| Preservation of author work | 10/10 | `LPic1.md` remains the long-form source; correct explanations are retained and only confirmed errors or unsafe examples are corrected. |
| Technical accuracy | 10/10 | Commands and concepts were checked against the official LPI scope and upstream manuals listed in `REFERENCES.md`. |
| Beginner clarity | 10/10 | Chapters introduce the concept before commands and explain important arguments, verification and failure modes. |
| Command safety | 10/10 | Destructive storage, boot, service and network tasks include target verification, rollback or lab-only warnings. |
| Hands-on practice | 10/10 | Every topic has a chapter lab, plus 23 cross-objective lab scenarios in `labs/README.md`. |
| Exercises | 10/10 | Every topic has review questions and the repository includes a 90-point, 40-item mixed assessment. |
| Answer coverage | 10/10 | Every chapter question and every mixed-assessment item has a separate explained answer. |
| Navigation and Markdown | 10/10 | README study path, objective matrix, relative links, fenced code blocks and tables pass the repository checks. |
| Official references | 10/10 | LPI objectives and upstream Linux/GNU/project documentation are collected separately from the teaching text. |

## Verification summary

- Active official objectives in the coverage matrix: **42**
- Matching objective headings in chapters: **42**
- Dedicated topic chapters: **10**
- Additional hands-on labs: **23**
- Mixed assessment: **40 items / 90 points**
- Markdown structural lint result: **0 errors**
- Missing internal links, excluding the preserved root notebook during local
  pre-publish validation: **0**

## Honest limitation

LPIC objectives name knowledge areas and a partial list of commands; they do not
publish the live exam question bank. This guide covers the published scope, but
readers should still practice on current Debian-family and RPM-family systems,
read the local manual pages, and verify the official objectives before booking
an exam.
