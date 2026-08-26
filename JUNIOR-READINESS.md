# LPIC-1 and Junior Linux Readiness

Reading the chapters is necessary but not sufficient. LPIC-1 tests published
Linux administration knowledge; a junior role also requires safe execution,
output interpretation, troubleshooting discipline and the ability to explain
what changed.

Use this file as a practical exit checklist after completing the
[objective matrix](OBJECTIVES.md).

## Readiness gates

A learner is ready to claim solid LPIC-1-level preparation when all of these
are true:

1. Every active objective is complete under the five-part rule in
   [OBJECTIVES.md](OBJECTIVES.md#completion-rule).
2. Every chapter exercise was answered before reading its explanation.
3. Both timed mocks score at least 54/60 on two attempts separated by several
   days, with no answer based only on memorizing the previous key.
4. All destructive labs were performed only on disposable storage/VMs and the
   learner can explain the rollback.
5. The learner can diagnose the scenarios below from evidence before proposing
   a change.

The 54/60 gate is deliberately strict and is not LPI's confidential passing
formula.

## Practical competency checklist

| Done | Area | Demonstrate without following a recipe | Required evidence |
|---|---|---|---|
| [ ] | Hardware | Map one PCI and one USB device from bus listing to driver/sysfs/device node | `lspci -nnk`, `lsusb -t`, `/sys`, `/dev`, explanation |
| [ ] | Boot | Reconstruct firmware → bootloader → kernel/initramfs → real root → PID 1 | `/proc/cmdline`, journal, PID 1, boot sequence |
| [ ] | Targets | Inspect/change a lab default target, schedule/cancel shutdown, recover safely | before/after output and console plan |
| [ ] | Layout | Design workstation, log-server and database layouts | mount/LVM/swap choices and failure-domain reasoning |
| [ ] | GRUB | Identify source versus generated configuration and produce a safe test config | firmware mode, files, command output, recovery plan |
| [ ] | Libraries | Diagnose one “library not found” scenario without globally weakening search paths | `file`, `ldd`, `ldconfig`, search-order explanation |
| [ ] | Debian packages | Query, install, own-file search, verify, remove/purge and inspect the transaction | APT/dpkg transcript and package state |
| [ ] | RPM packages | Perform equivalent query/install/verify/remove work with DNF/RPM | DNF/RPM transcript and interpretation |
| [ ] | VM cloning | Prove two test clones have unique machine IDs and SSH host keys | fingerprints and provisioning explanation |
| [ ] | Shell | Explain quoting, expansion, environment inheritance, PATH and history risks | small commands with predicted output |
| [ ] | Filters | Build a report using fields, sorting, adjacent de-duplication and checksums | input, pipeline, validated output |
| [ ] | Files | Safely find/copy/archive unusual filenames including spaces/newlines | NUL-safe command and extraction verification |
| [ ] | Streams | Predict results of differently ordered stdout/stderr redirects | separate test outputs and explanation |
| [ ] | Processes | Manage jobs, inspect states, use TERM before KILL and detach a session | PID proof, signals and cleanup |
| [ ] | Priority | Show default nice value, lower a process priority and explain privilege limits | `ps` before/after and scheduler caveat |
| [ ] | Regex | Write BRE, ERE and fixed-string matches and a non-destructive sed transform | sample input and expected output |
| [ ] | vi | Navigate, search, edit, yank/paste, undo, save and discard | completed practice file without another editor |
| [ ] | Storage | Partition/format/mount a dedicated disposable disk and validate fstab | target proof, UUID entry, `findmnt` verification |
| [ ] | Filesystem | Diagnose block versus inode exhaustion and choose an offline repair method | `df`, `du`, inode data and no unsafe repair |
| [ ] | Permissions | Build a setgid team directory and test with two users and three umasks | modes, ownership and observed access |
| [ ] | Links/FHS | Predict inode/link behavior and place example files under appropriate FHS paths | `ls -li` proof and placement explanation |
| [ ] | Bash scripting | Write a checked script using functions, arguments, loops, tests and statuses | success/failure tests plus `bash -n` |
| [ ] | Desktop | Identify X11/Wayland, display manager, desktop, auth model and remote options | session data without using `xhost +` |
| [ ] | Accounts | Create/modify/age/lock/remove an account without losing unrelated groups/data | `getent`, `id`, aging output and cleanup audit |
| [ ] | Scheduling | Run one harmless task through cron, at and a systemd timer | execution evidence and environment comparison |
| [ ] | Locale/timezone | Demonstrate locale precedence, predictable C-locale parsing and timezone change | environment and before/after time output |
| [ ] | Time sync | Distinguish system clock, RTC, zone and NTP synchronization health | Chrony/NTP source and tracking evidence |
| [ ] | Logging | Route/tag/query/rotate a lab message and read an offline journal | validated configs and retrieved records |
| [ ] | Mail/printing | Explain aliases/forwarding/queue state and inspect a CUPS queue | non-production lab output and commands |
| [ ] | IP | Calculate IPv4 networks and explain IPv6 link-local/ICMPv6 behavior | manual calculation and command verification |
| [ ] | Persistent network | Inspect and safely create a lab NetworkManager profile | profile, address, route, DNS and rollback |
| [ ] | Troubleshooting | Diagnose link → address → route → socket/firewall → DNS → application | evidence at each layer; one change at a time |
| [ ] | DNS | Explain why `dig`, `host` and `getent` can disagree | NSS/resolver files and queries |
| [ ] | Host audit | Review special-bit files, listeners, services, limits, logins and sudo policy | findings classified as expected or actionable |
| [ ] | SSH | Verify host identity, use an agent/key and create a loopback-only tunnel | fingerprints, effective config and test |
| [ ] | GnuPG | Generate/revoke a disposable key; encrypt/decrypt and sign/verify | successful round trips and trust explanation |

## Troubleshooting discipline

For each failure, write the following before changing configuration:

1. Observed symptom and exact command/output
2. Last known good state and recent change
3. Current layer and two competing hypotheses
4. Read-only test that distinguishes those hypotheses
5. Smallest reversible correction
6. Verification and rollback result

Random command sequences are not troubleshooting. If a proposed command cannot
be connected to evidence and a hypothesis, gather more evidence first.

## Scope boundary

Completing this repository supports the published LPIC-1 scope and a strong
junior Linux foundation. It does not claim to cover every employer's junior
role. Jobs may additionally require Git, virtualization platforms, cloud/IaC,
containers in depth, firewalls, SELinux/AppArmor, web/database services,
monitoring, ticketing and organization-specific procedures.
