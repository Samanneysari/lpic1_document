# LPIC-1 101-500 Mock Exam A — Answer Key

Score one point per answer. A guessed correct answer still marks a review need.

## Topic 101 answers

1. **B** — `/sys` exposes the structured kernel device/driver model.
2. **C** — `lspci -nnk` includes numeric PCI IDs and kernel-driver data.
3. **B** — Firmware selects the boot path; bootloader loads kernel/initramfs;
   early userspace finds real root; the kernel then starts PID 1.
4. **A** — `journalctl -b` restricts output to the current boot.
5. **`/proc/cmdline`** — It contains the command line passed to the running kernel.
6. **B** — `set-default` changes the target selected for future normal boots.
7. **B** — Isolating rescue mode can stop units that provide the SSH connection.
8. **B** — `wall`, scheduled `shutdown -r`, and `shutdown -c` perform the three steps.

## Topic 102 answers

9. **B** — Separation helps policy/capacity but is not an independent copy.
10. **C** — Storage becomes a PV, PVs form a VG, and LVs allocate from the VG.
11. **C** — `grub.cfg` is generated from administrator/distribution source files.
12. **C** — UEFI loads a registered or fallback EFI executable from the ESP.
13. **`ldd`** — Use it only on a trusted executable.
14. **B** — `dpkg -S` searches installed path ownership.
15. **B** — It downloads current repository indexes/metadata.
16. **A** — `apt-file` searches a downloaded package-contents index.
17. **B** — `rpm -qf PATH` queries the installed owner of a file.
18. **B** — Verification differences need investigation; legitimate changes occur.
19. **C** — Repository managers resolve dependencies; low-level RPM does not do so
    in the same way.
20. **B** — Duplicate machine identity and host keys break unique identity/trust.

## Topic 103 answers

21. **B** — Single quotes preserve their contents literally.
22. **C** — `type` understands builtins, functions, aliases and executable resolution.
23. **B** — `export` places the variable in child-process environments.
24. **`~/.bash_history`** — Bash commonly writes persistent interactive history there.
25. **A** — `uniq` compares neighboring records, so unsorted duplicates can remain.
26. **B** — `xzcat` sends decompressed data to stdout.
27. **B** — `-type f` selects regular files and `+10M` means larger than 10 MiB units.
28. **C** — NUL delimiters preserve spaces, newlines and other pathname characters.
29. **C** — Uppercase `J` selects xz in GNU tar.
30. **B** — `of=` is the output target; reversing it can destroy data.
31. **C** — File descriptor 2 is stderr.
32. **B** — stdout is opened on `out`; stderr is then duplicated to stdout's destination.
33. **A** — `tee` writes its input to stdout and one or more files.
34. **B** — `xargs` builds command arguments from input records.
35. **B** — `jobs` reports the current shell's job table.
36. **C** — SIGTERM normally permits orderly cleanup.
37. **A** — `-x` requires an exact process name; inspect with `pgrep -a -x` first.
38. **B** — Both terminal multiplexers support detached interactive sessions.
39. **C** — The normal default is 0, subject to inherited/process policy.
40. **C** — Lowering the numeric nice value raises priority and normally needs privilege.
41. **A** — Anchors require a whole-line match and ERE parentheses/`|` express alternation.
42. **B** — `grep -F` performs fixed-string matching.
43. **B** — Without `-i`, sed writes the transformed stream to stdout.
44. **B** — `yy` yanks the current line.
45. **C** — `:q!` abandons unsaved changes and quits.
46. **C** — Many tools consult `EDITOR`; some also prefer `VISUAL`.

## Topic 104 answers

47. **A** — `gdisk` is GPT-focused.
48. **B** — A Btrfs subvolume is a separate filesystem tree root, not a partition.
49. **A** — Inode exhaustion can block creation even when blocks remain.
50. **B** — `-n` requests no modification in `xfs_repair`.
51. **D** — The sixth fstab field is the filesystem-check pass number.
52. **B** — UUIDs remain stable across normal device enumeration changes.
53. **C** — systemd escapes the path into `srv-data.mount`.
54. **B** — Leading 2 is setgid; both owner and group receive 7.
55. **A** — `666 & ~027` produces `640` for the usual requested mode.
56. **B** — `chgrp` changes group ownership.
57. **C** — Hard-linked names reference the same inode and cannot cross filesystems.
58. **B** — `-s` requests a symbolic link; target comes before link name.
59. **B** — The locate database can lag filesystem changes until `updatedb` runs.
60. **A** — `/etc` is for host-specific system configuration.

## Review method

For every missed or guessed item, record its objective code, explain why each
distractor is wrong, perform the mapped lab step, then retake only after a gap
of at least one day.
