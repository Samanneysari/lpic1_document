# LPIC-1 Hands-on Labs

These labs complement the chapter labs. Perform storage, boot and network-changing tasks only in disposable VMs with console access and snapshots.

## Lab workflow

For every lab, submit:

1. Objective and starting state
2. Commands used
3. Important output
4. Verification
5. One introduced failure and diagnosis
6. Cleanup
7. What you learned

## Exam 101 labs

### LAB-101-1: Hardware inventory

- Record firmware mode, CPU architecture, memory, PCI/USB devices and block devices.
- Map one PCI device to its kernel driver.
- Identify one `/sys` path and one `/dev` node for a device.
- Verify with `lspci -nnk`, `lsusb -t`, `lscpu`, `free -h`, `lsblk` and `udevadm info`.

### LAB-101-2: Boot evidence

- Reconstruct the current boot using `/proc/cmdline`, `dmesg`, `journalctl -b` and PID 1.
- Identify one warning, decide whether it is actionable and cite evidence.
- Compare current and previous boot journals when available.

### LAB-101-3: Targets and shutdown

- Identify the default target and graphical/multi-user dependency chains.
- Schedule and cancel a reboot after warning logged-in users.
- Do not isolate rescue mode without console access.

### LAB-102-1: Disk-layout design

- Design layouts for a workstation, log server and small database server.
- Justify separate filesystems, LVM and swap choices.
- Explain failure and growth trade-offs; no commands modify disks.

### LAB-102-2: GRUB inspection and recovery plan

- Identify firmware mode, ESP when present, GRUB packages and generated configuration.
- Generate a test configuration under `/tmp` without replacing the active one.
- Write a recovery plan before changing any boot setting.

### LAB-102-3: Package equivalence

- Use one Debian and one RPM-family VM.
- Refresh metadata; query, install, verify ownership and remove `tree`.
- Compare APT, dpkg, DNF/RPM and optionally Zypper commands.

### LAB-102-4: Clone identity audit

- Clone a prepared lab VM twice.
- Compare machine ID, product UUID, SSH host-key fingerprints, hostname, MAC address and cloud-init state.
- Record which values must be unique and repair the template using its supported preparation process.

### LAB-103-1: Command-line and filters

- Build a report from a copy of `/etc/passwd` using `cut`, `sort`, `uniq`, `wc`, `head` and `tail`.
- Keep stdout and stderr separate.
- Verify record counts.

### LAB-103-2: Files and archives

- Create a tree containing spaces, hidden files and unusual names.
- Copy with metadata, find safely, archive, list before extraction and verify SHA-256 after extraction.
- Explain how null delimiters protect filenames.

### LAB-103-3: Jobs and processes

- Start foreground and background jobs.
- Stop/continue them, inspect parent relationships and send SIGTERM.
- Use `nice`/`renice` and record limits for an unprivileged account.

### LAB-103-4: Regex and vi

- Create a mixed configuration file.
- Select comments, blank lines, IPv4-like text and exact keywords with BRE/ERE/fixed strings.
- Use vi to edit, search, yank, paste, undo, save and quit.

### LAB-104-1: Disposable filesystem

- Attach a dedicated empty virtual disk.
- Partition, format, label, mount and verify it.
- Add a UUID fstab entry, run `findmnt --verify`, test, then clean up.
- Get a second-person check before `mkfs`.

### LAB-104-2: Permissions and collaboration

- Create a shared group directory using setgid.
- Test owner/group/other access with two users.
- Compare file and directory results under umask 022, 027 and 077.
- Create and inspect hard and symbolic links.

## Exam 102 labs

### LAB-105-1: Shell environment

- Add an idempotent `$HOME/bin` PATH change, one alias and one function.
- Prove behavior in login and interactive non-login shells.
- Inspect `/etc/skel` without adding secrets.

### LAB-105-2: Defensive Bash script

- Build a system-report script with argument validation, functions, loop, condition, redirection and meaningful exit statuses.
- Test missing, invalid and valid inputs.
- Validate with `bash -n` and ShellCheck when available.

### LAB-106-1: Desktop session

- Identify X11/Wayland, display manager, desktop and relevant environment.
- Review access controls without using `xhost +`.
- Test and restore one accessibility feature.

### LAB-107-1: Account lifecycle

- Create a user explicitly, set groups and aging, lock/unlock and verify each state.
- Compare `getent`, `id`, passwd and shadow information.
- Search for remaining UID-owned files before cleanup.

### LAB-107-2: Three schedulers

- Run equivalent harmless reporting tasks with cron, `at` and a systemd timer.
- Verify execution through output/logs.
- Compare environment, missed-run behavior and management commands.

### LAB-108-1: Logs and rotation

- Route a tagged local facility into a lab file.
- Validate rsyslog before reload.
- Query journal by unit, tag, time and priority.
- Debug a logrotate policy, force it only on disposable logs and clean up.

### LAB-109-1: Layered troubleshooting

- Capture healthy baseline information.
- Introduce one fault at a time: down interface, wrong prefix, missing route, wrong resolver and stopped service.
- Diagnose from link to application without changing unrelated settings.

### LAB-109-2: DNS path

- Compare `/etc/hosts`, `getent`, `host`, `dig`, a chosen resolver and systemd-resolved when present.
- Record status, answer, authority and TTL.
- Explain a case where `dig` succeeds but the application lookup fails.

### LAB-110-1: Host audit

- Inventory special-permission files, listening sockets, enabled services, login history and sudo access.
- Select one finding and verify whether it is expected through package/configuration evidence.
- Do not scan external targets.

### LAB-110-2: SSH and GPG

- Verify an SSH host fingerprint, create a passphrase-protected key and use `ssh-agent`.
- Test a loopback-only tunnel.
- Generate a disposable GPG key, encrypt/decrypt, sign/verify and create a revocation certificate.
- Remove disposable secrets securely according to lab policy.

## Completion criteria

A lab is complete only when the final verification succeeds and cleanup is documented. A screenshot alone is not sufficient evidence; include commands and interpreted output.
