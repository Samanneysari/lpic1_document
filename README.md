# LPIC-1 Complete Study Guide

This repository is a beginner-friendly, objective-aligned study guide for Linux Professional Institute LPIC-1 version 5.0:

- Exam 101-500
- Exam 102-500

The guide explains concepts before commands, breaks important commands into their parts, includes safe hands-on labs, and provides exercises plus two weighted 60-question mock exams with separate answer keys.

> [!IMPORTANT]
> The original author notes remain available in [`LPic1.md`](LPic1.md), but the
> objective-aligned chapters below are the primary study path. Useful original
> explanations are preserved and confirmed technical mistakes are corrected.

## Start here

1. Read [How to use this guide](docs/00-how-to-use-this-guide.md).
2. Follow the chapters in objective order.
3. Use the [worked-example companion](worked-examples/README.md) after each objective. It provides 126 beginner-friendly examples, with every command line explained.
4. Perform labs only on a disposable virtual machine.
5. Complete the exercises before opening the answer key.
6. Use the [coverage matrix](OBJECTIVES.md) to track progress.
7. Finish with the [junior-readiness checklist](JUNIOR-READINESS.md) and both timed mocks.

## Exam 101-500

| Topic | Chapter | Main skills |
|---|---|---|
| 101 | [System Architecture](docs/101-system-architecture.md) | Hardware, boot, kernel modules, runlevels and targets |
| 102 | [Linux Installation and Package Management](docs/102-installation-package-management.md) | Disk layout, GRUB, libraries, Debian/RPM tools, virtualization |
| 103 | [GNU and Unix Commands](docs/103-gnu-unix-commands.md) | Shell, filters, files, streams, processes, regex and vi |
| 104 | [Devices, Filesystems and FHS](docs/104-devices-filesystems-fhs.md) | Partitions, filesystems, mounts, permissions, links and FHS |

## Exam 102-500

| Topic | Chapter | Main skills |
|---|---|---|
| 105 | [Shells and Shell Scripting](docs/105-shells-shell-scripting.md) | Shell environment, functions and Bash scripts |
| 106 | [User Interfaces and Desktops](docs/106-user-interfaces-desktops.md) | X11, Wayland, desktops, remote display and accessibility |
| 107 | [Administrative Tasks](docs/107-administrative-tasks.md) | Users, groups, cron, at, systemd timers, locale and time zones |
| 108 | [Essential System Services](docs/108-essential-system-services.md) | Time sync, logging, mail and printing |
| 109 | [Networking Fundamentals](docs/109-networking-fundamentals.md) | TCP/IP, persistent configuration, troubleshooting and DNS |
| 110 | [Security](docs/110-security.md) | Host auditing, service hardening, SSH and GnuPG |

## Practice material

- [126 line-by-line worked examples](worked-examples/README.md)
- [Hands-on labs](labs/README.md)
- [Chapter exercises and mock questions](exercises/questions.md)
- [Answer key and explanations](exercises/answers.md)
- [Timed mock 101-500](exercises/mock-101.md) and [explained answers](exercises/mock-101-answers.md)
- [Timed mock 102-500](exercises/mock-102.md) and [explained answers](exercises/mock-102-answers.md)
- [LPIC-1 and junior Linux readiness](JUNIOR-READINESS.md)
- [Command safety checklist](SAFETY.md)
- [Official references](REFERENCES.md)
- [Quality check and completion evidence](QUALITY-CHECK.md)

## Standard chapter structure

Each chapter follows the same learning sequence:

1. What the topic is
2. Why it matters
3. Core theory
4. Commands and configuration
5. Command breakdown
6. Verification
7. Common mistakes and troubleshooting
8. Security notes
9. Lab
10. Exercises

## Lab requirements

Two small virtual machines are enough for most labs:

| VM | Suggested OS | CPU | RAM | Disk | Purpose |
|---|---|---:|---:|---:|---|
| `lpic-debian` | Debian 12 or Ubuntu LTS | 2 vCPU | 2 GB | 25 GB | Debian tools, systemd, networking and scripts |
| `lpic-rpm` | Rocky Linux 9 or AlmaLinux 9 | 2 vCPU | 2 GB | 25 GB | RPM, DNF, SELinux-aware administration and cross-distribution practice |

Add a separate disposable virtual disk to a VM for partitioning exercises. Never practice `fdisk`, `mkfs`, `wipefs`, or filesystem repair on a disk containing important data.

## Scope and sources

The canonical scope is the [official LPI LPIC-1 objectives](https://www.lpi.org/our-certifications/exam-101-102-objectives/). Technical behavior is cross-checked against upstream manuals and official project documentation listed in [REFERENCES.md](REFERENCES.md).

The currently published objectives are version 5.0 (`101-500` and `102-500`).
LPI describes each exam as 60 multiple-choice/fill-in questions in 90 minutes;
the two timed mocks mirror that public format and objective-weight distribution.
No independent guide can guarantee the unpublished live questions or every
employer's junior interview scope.

This is an independent study guide and is not an official LPI publication.

## Repository validation

Run the dependency-free structural check after editing study content:

```bash
python3 scripts/check_repo.py
```

It verifies all 42 objective headings/mappings, the two 60-question mock and
answer sequences, chapter/mixed question counts, code fences and relative links.
