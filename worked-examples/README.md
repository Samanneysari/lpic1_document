# LPIC-1 Worked Examples

This layer closes the main beginner gap in the study guide: every official LPIC-1 v5.0 objective now has three small examples, and every command line is explained immediately after it. That gives you 126 fully explained examples across all 42 active objectives.

## How to use it

1. Read one objective in the main chapter.
2. Run its three worked examples in a disposable Linux VM.
3. Read the explanation only after predicting what each command part means.
4. Compare your real output with the verification note. Different names and versions are normal.
5. Complete the practice task and keep a short lab journal.
6. Continue with the linked repository lab and assessment questions.

## Chapters

- [101: System Architecture](101.md)
- [102: Linux Installation and Package Management](102.md)
- [103: GNU and Unix Commands](103.md)
- [104: Devices, Linux Filesystems, and the FHS](104.md)
- [105: Shells and Shell Scripting](105.md)
- [106: User Interfaces and Desktops](106.md)
- [107: Administrative Tasks](107.md)
- [108: Essential System Services](108.md)
- [109: Networking Fundamentals](109.md)
- [110: Security](110.md)

## Important safety rule

The worked examples favor observation and temporary files. Disk creation, filesystem repair, bootloader installation, account changes, network reconfiguration, shutdown, and security-policy changes belong only in a disposable VM with a snapshot and console access. Never replace an example device or path by guessing.

## What this layer does and does not do

The main `docs/` chapters remain the source for complete theory, command families, configuration formats, failure modes, and exam scope. These worked examples add slow, explicit command reading for first-time learners. The `labs/` directory adds multi-step practice, and `exercises/` tests recall and reasoning. Use all three layers; examples alone are not a complete preparation method.
