# LPIC-1 102-500 Mock Exam A — Answer Key

Score one point per answer. A guessed correct answer still marks a review need.

## Topic 105 answers

1. **B** — Bash tries `.bash_profile`, `.bash_login`, then `.profile`, stopping
   at the first readable user login file.
2. **B** — Sourcing runs commands in the current shell, so they can alter it.
3. **B** — A malicious same-name executable in the current directory may win.
4. **C** — Skeleton content is copied during future home creation when enabled.
5. **B** — The shebang requests the script interpreter.
6. **B** — Quoted `$@` preserves each positional parameter as a separate word.
7. **A** — `&&` evaluates its right side only after a zero status.
8. **B** — The kernel generally refuses the unsafe interpreted-setuid model;
   use narrow sudo policy or a purpose-built helper.

## Topic 106 answers

9. **B** — The X server owns display/input resources and serves client programs.
10. **A** — `xauth` manages cookies and `DISPLAY` selects the server/display/screen.
11. **A** — SPICE is common for virtual-machine remote consoles.
12. **B** — Repeat-key settings control automatic repetition while a key remains
    held; bounce keys instead reject rapid separate presses.

## Topic 107 answers

13. **B** — `getent` follows `/etc/nsswitch.conf` and can query LDAP or other sources.
14. **B** — `-aG` appends; `-G` alone replaces the supplementary group list.
15. **B** — Password locking does not inherently disable keys, tokens or all services.
16. **`chage`** — It queries and changes password-aging fields.
17. **B** — Least privilege means no interactive authentication and narrow access.
18. **B** — Minute, hour, day of month, month and day of week precede the command.
19. **B** — A system crontab selects the account in an additional field.
20. **B** — `atrm JOB_ID` removes a queued job; `atq` lists jobs.
21. **B** — A calendar event missed during downtime may run after activation.
22. **B** — `LC_ALL` overrides category-specific variables and `LANG`.
23. **A** — The C locale makes parsing, collation and messages more predictable.
24. **B** — `-f` specifies input encoding and `-t` output encoding.

## Topic 108 answers

25. **B** — `--systohc` writes system time to RTC; `--utc` records its interpretation.
26. **C** — NTP normally uses UDP 123.
27. **A** — `chronyc sources -v` reports candidates and selection state.
28. **B** — A syslog priority selector normally includes that level and more urgent ones.
29. **C** — Persistent journal files normally live below `/var/log/journal/`.
30. **`--directory`** — It points journalctl at an offline journal directory.
31. **A** — Debug mode parses and explains actions without rotating files.
32. **B** — `newaliases` rebuilds the database used for local aliases.
33. **B** — `.forward` requests per-user forwarding subject to MTA policy.
34. **B** — It displays queued outbound/local transfers, not a user's mailbox.
35. **A** — `lpq` lists jobs through the legacy-compatible interface.
36. **B** — `lpadmin -x` deletes the named queue, not the physical device.

## Topic 109 answers

37. **C** — A `/27` has blocks of 32; 77 falls within 64–95.
38. **B** — SSH uses TCP 22 by default.
39. **C** — TCP supplies sequencing, acknowledgment and retransmission.
40. **B** — IPv6 link-local unicast is `fe80::/10`; Neighbor Discovery uses multicast.
41. **B** — The `hosts:` line defines resolver/NSS source order.
42. **A** — It lists saved/active NetworkManager profiles.
43. **A** — `--ask` prompts rather than recording a plaintext argument in history.
44. **A** — Administrator networkd units normally live under that directory.
45. **A** — `ip route get` performs a kernel route lookup without adding a route.
46. **A** — The flags request listening, numeric, TCP/UDP and process information.
47. **B** — Filtering one protocol does not prove the destination/application is down.
48. **B** — Legacy `route` displays/changes the IPv4 routing table.
49. **C** — `getent` follows NSS; `dig` and `host` make DNS queries.
50. **A** — Inspect `hosts:` ordering and action clauses there, then local resolver state.

## Topic 110 answers

51. **A** — `-perm -4000` requires the setuid bit in the mask.
52. **B** — `visudo` locks and validates sudoers syntax.
53. **B** — `w` combines sessions, activity and load summaries.
54. **B** — `/etc/passwd` normally holds an `x` placeholder; hashes are protected in shadow.
55. **A** — Socket activation can start a service on demand despite service disablement.
56. **A** — Many current programs are not linked to or do not consult TCP wrappers.
57. **B** — A changed enrolled host key warns of replacement, reinstallation or attack.
58. **C** — `ssh -D` creates a dynamic local SOCKS listener.
59. **B** — A signature supports integrity/authenticity only after trustworthy key binding.
60. **`ssh-add`** — It requests loading a key into the agent after any required passphrase.

## Review method

For every missed or guessed item, record its objective code, explain why each
distractor is wrong, perform the mapped lab step, then retake only after a gap
of at least one day.
