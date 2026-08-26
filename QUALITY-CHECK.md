# LPIC-1 Quality Check

Last objective review: **2026-08-26**

This is an evidence record, not an official LPI endorsement and not a guarantee
of an exam or employment result.

## Scope baseline

- Official objective version: **5.0**
- Exam codes: **101-500** and **102-500**
- Active published objectives: **42** (`104.4` is removed)
- Public exam format: **60 questions / 90 minutes per exam**
- Canonical source: [LPI Exam 101 and 102 Objectives](https://www.lpi.org/our-certifications/exam-101-102-objectives/)

## Repository evidence

| Check | Result | Evidence |
|---|---|---|
| Objective headings | Pass | All 42 active objectives have matching chapter sections. |
| Fine-grained scope | Pass | `OBJECTIVES.md` maps every objective's knowledge areas and named official scope to chapter/lab evidence. |
| Objective-version match | Pass | Repository and official current pages both identify version 5.0 and codes 101-500/102-500. |
| Exam 101 practice | Pass | `mock-101.md` has 60 original questions allocated exactly by objective weight, with a separate explained key. |
| Exam 102 practice | Pass | `mock-102.md` has 60 original questions allocated exactly by objective weight, with a separate explained key. |
| Additional questions | Pass | 71 chapter questions plus a 40-item mixed assessment with explained answers. |
| Hands-on work | Pass | Ten chapter labs plus 23 additional objective labs; all destructive work is explicitly lab-only. |
| Junior readiness | Pass | `JUNIOR-READINESS.md` requires command evidence, troubleshooting, rollback and two timed-mock gates. |
| Technical corrections | Pass | BRE/ERE alternation, APT upgrade behavior, symlink modes and missing official terms were corrected in this review. |
| Destructive-command safety | Pass | Storage, boot, service, network and key-management sections include verification or recovery cautions. |
| Source separation | Pass | Official/upstream references are collected in `REFERENCES.md`; live exam questions are not claimed or copied. |

## Quantitative inventory

- Objective-aligned chapters: **10**
- Active objective sections: **42**
- Chapter labs: **10**
- Additional lab scenarios: **23**
- Chapter review questions: **71**
- Mixed assessment: **40 items / 90 points**
- Timed mocks: **2 × 60 questions**
- Total question items: **231**

## What “complete” means here

The repository covers every currently published LPIC-1 version 5.0 knowledge
area and named file/term/utility at an appropriate introductory depth. It gives
learners a path to practice and verify that scope.

It does **not** mean:

- possession of LPI's unpublished live question bank;
- a promise that reading alone produces operational skill;
- coverage of every command option or every Linux distribution;
- coverage of every employer's junior Linux, cloud or DevOps interview;
- a substitute for current local manuals and supervised hands-on work.

## Remaining maintenance risks

1. LPI may publish a later objective version. Recheck the canonical English
   objective page before booking an exam.
2. Command behavior and configuration paths vary by distribution and release.
3. Examples must be revalidated as Debian-family, RPM-family, systemd,
   NetworkManager, OpenSSH and other upstream versions change.
4. Practice-item quality benefits from fresh reviewers; ambiguous items should
   be fixed rather than defended.
