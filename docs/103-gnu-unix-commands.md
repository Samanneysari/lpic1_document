# Topic 103: GNU and Unix Commands

Topic 103 carries substantial exam weight. Practice every command in a normal user account before using privileged paths.

## 103.1 Work on the command line

If `ls`, `cd`, paths and files are completely new, first try the [first shell session](00-linux-foundations.md#4-your-first-shell-session).

### Command parsing

The shell reads text, applies quoting and expansions, performs redirections, and then executes a built-in, function or external program.

```bash
printf '%s\n' "Home: $HOME"
```

| Part | Meaning |
|---|---|
| `printf` | Predictable formatted-output command |
| `'%s\n'` | Single quotes preserve the format literally |
| `"Home: $HOME"` | Double quotes keep the text as one argument but allow variable expansion |

Quoting rules:

- Unquoted text is subject to word splitting and pathname expansion.
- Single quotes preserve every character until the next single quote.
- Double quotes allow `$variable`, `$(command)` and selected backslash processing while preventing normal word splitting and glob expansion.
- A backslash protects the next character outside single quotes.

```bash
name='Ada Lovelace'
printf '%s\n' "$name"
printf '%s\n' '$name'
```

The first `printf` displays the value. The second displays the literal characters `$name`.

### Command sequences

```bash
mkdir -p practice && cd practice
test -f report.txt || touch report.txt
```

| Operator | Behavior |
|---|---|
| `;` | Runs the next command regardless of status |
| `&&` | Runs the next command only after success (status 0) |
| `\|\|` | Runs the next command only after failure (nonzero status) |

### Environment and shell variables

```bash
course=LPIC1
export course
env | grep '^course='
unset course
```

A shell variable exists in the current shell. `export` marks it for inheritance by subsequently started processes. Child processes cannot modify the parent shell's variables.

Useful commands:

```bash
pwd
echo "$SHELL"
type cd
type -a python
which ls
command -v ls
uname -a
history 10
```

`type` understands built-ins, aliases, functions and hashed commands. `which` searches executable paths but may not describe shell built-ins consistently. `command -v` is useful in portable shell scripts.

`echo` is a commonly tested shell builtin for simple output, but its handling
of options and backslash escapes varies. Prefer `printf` when exact portable
formatting matters.

`ls` lists entries in a directory (`ls -l` adds detailed columns). `cd` changes the current shell's directory (`cd ..` moves to its parent). `pwd` prints where you are. On some systems `ll` is a user-defined alias, often for `ls -l`; it is not a portable command. Confirm with `type ll` before relying on it. An **alias** is a short name expanded by an interactive shell, not a new executable:

```bash
alias ll='ls -l'
```

`alias` defines the name; `ll` is the name; `'ls -l'` is the replacement. Run `type ll` to check it. This definition lasts for the current shell only; shell startup files can define it for later sessions. In scripts, call `ls -l` explicitly instead of assuming aliases are enabled.

`PATH` is a colon-separated search list:

```bash
printf '%s\n' "$PATH" | tr ':' '\n'
```

The current directory is not searched unless represented in `PATH`; execute a local script explicitly as `./script.sh`.

### History

```bash
history
history 20
!!
!42
Ctrl+R
```

`!!` repeats the previous command, `!42` recalls history entry 42, and `Ctrl+R` starts an interactive reverse search. Inspect recalled destructive commands before executing them. Bash commonly saves persistent history in `~/.bash_history` when the shell exits.

### Documentation

```bash
man 1 passwd
man 5 passwd
apropos 'copy files'
whatis chmod
info coreutils
```

Manual section matters: `passwd(1)` is a command, while `passwd(5)` describes the file format.

## 103.2 Process text streams with filters

A filter reads records, transforms or selects them, and writes a result. Unless documented otherwise, filters do not edit the original file.

### Viewing and selecting

`cat` prints a whole file; `head` prints the beginning; `less` lets you scroll in either direction without loading a file into an editor. The older `more` is also a pager and commonly moves forward one screen at a time. `most` is an optional pager and may need a separate package; do not expect it on every host. In `less`, press `Space` for the next page, `b` for the previous page, `/word` to search and `q` to leave.

```bash
head -n 3 /etc/passwd
```

`head` selects the start of a file; `-n 3` asks for three lines; `/etc/passwd` contains public account metadata, not plaintext passwords. Each output line is one account record.

```bash
nl -ba /etc/passwd | less
```

`nl` numbers lines; `-ba` also numbers blank lines; `|` hands the numbered output to `less` for scrolling. Press `q` to leave. For a short file, `more /etc/passwd` is another way to page through it.

```bash
more /etc/passwd
```

`more` opens this account file one screen at a time; press `Space` to advance and `q` to exit. If `most` is installed, `most /etc/passwd` opens the same file in that optional pager; use `command -v most` to see whether it is available. Pager keys can differ, so use its help screen when needed.

```bash
cat file.txt
nl -ba file.txt
head -n 5 file.txt
tail -n 20 file.txt
tail -f /var/log/example.log
less file.txt
```

`tail -f` follows appended data until interrupted. `less` is interactive; use `/pattern` to search, `n` for the next match and `q` to quit.

### Fields and columns

Given `users.csv`:

```text
alice,engineering,active
bob,support,inactive
```

```bash
cut -d, -f1,3 users.csv
```

| Option | Meaning |
|---|---|
| `-d,` | Uses comma as the field delimiter |
| `-f1,3` | Selects fields 1 and 3 |

Combine corresponding lines:

```bash
paste names.txt roles.txt
join -t, -1 1 -2 1 sorted-a.csv sorted-b.csv
```

`join` expects both inputs sorted on the join field unless the data naturally satisfies that requirement.

### Transforming and sorting

```bash
tr '[:lower:]' '[:upper:]' < file.txt
sort -u file.txt
sort -t: -k3,3n /etc/passwd
uniq -c sorted.txt
wc -l -w -c file.txt
```

`uniq` removes or counts adjacent duplicate lines; sort first when duplicates may be separated.

```bash
printf '%s\n' pear apple pear | sort | uniq -c
```

`printf` creates three lines; the first pipe gives them to `sort`, which places identical names next to each other; the second pipe gives them to `uniq -c`, which counts adjacent equal lines. Expect `1 apple` and `2 pear` (spacing may vary).

### Binary and numeric views

```bash
od -An -tx1 -N16 file.bin
md5sum file.iso
sha256sum file.iso
sha512sum file.iso
```

Checksums detect accidental changes and can support integrity verification when the expected digest is obtained through a trusted channel. MD5 is not collision-resistant and should not be used as a modern security proof.

### Split and recombine

```bash
split -b 100M --numeric-suffixes image.iso image.part.
cat image.part.* > image.rebuilt.iso
sha256sum image.iso image.rebuilt.iso
```

### Read compressed streams

```bash
zcat file.gz
bzcat file.bz2
xzcat file.xz
```

These write decompressed content to standard output without replacing the compressed file.

## 103.3 Perform basic file management

### Create, copy, move and remove

In a disposable practice directory, these commands change names and contents, not the partition table:

```bash
touch note.txt
```

`touch` creates an empty `note.txt` if it does not exist. If it exists, `touch` updates its access and modification timestamps by default without replacing its contents. Check with `stat note.txt`.

```bash
mkdir -p drafts
```

`mkdir` creates a directory; `-p` accepts an existing directory and creates missing parent directories. `drafts` is relative to the current directory; check with `pwd` first.

```bash
cp -i note.txt drafts/note.txt
```

`cp` copies the source `note.txt` to the destination under `drafts`; `-i` asks before overwriting an existing destination. The original remains.

```bash
mv -i drafts/note.txt drafts/renamed.txt
```

`mv` moves or renames the source; `-i` asks before overwriting an existing destination. Verify that the old path is gone and the new path exists with `ls -l drafts`.

```bash
rm -i drafts/renamed.txt
```

`rm` removes that directory entry; `-i` asks for confirmation. It does not remove the `drafts` directory; `rmdir drafts` removes it if it is empty. Avoid `rm -r` until you understand recursive removal and have inspected the exact target.

```bash
mkdir -p project/{src,docs,backup}
touch project/docs/notes.txt
cp -a project/docs project/backup/
mv project/docs/notes.txt project/docs/readme.txt
rm -i project/docs/readme.txt
rmdir project/docs
```

| Option | Meaning |
|---|---|
| `mkdir -p` | Creates missing parent directories and tolerates existing ones |
| brace expression | Shell expands `{src,docs,backup}` into three names |
| `cp -a` | Archive mode: recursive copy while preserving common metadata |
| `rm -i` | Prompts before removal |
| `rmdir` | Removes empty directories only |

`rm` does not provide a standard recycle bin. Check expansions first:

```bash
printf '<%s>\n' project/*.txt
```

### Globbing

A **wildcard** is a character such as `*` used by the shell to expand matching pathnames *before* it runs a command. It is different from a regular expression used by `grep` or `sed`. Preview matches with `printf '<%s>\n' ./*.txt`; quotes around `./*.txt` would stop wildcard expansion. If nothing matches, default Bash can leave the literal pattern unchanged. Do not use an unchecked wildcard with `rm`.

| Pattern | Matches |
|---|---|
| `*` | Zero or more characters within one pathname component |
| `?` | Exactly one character |
| `[abc]` | One listed character |
| `[a-z]` | One character in a range, affected by locale |
| `[!0-9]` | One character not in the class |

Hidden names beginning with `.` are not matched by a leading `*` under normal Bash settings.

### Find files and act safely

```bash
find /var/log -type f -name '*.log' -mtime -7 -print
find . -type f -size +10M -exec ls -lh -- {} +
```

| Expression | Meaning |
|---|---|
| `-type f` | Regular files |
| `-name '*.log'` | Shell pattern protected from premature shell expansion |
| `-mtime -7` | Modified less than seven 24-hour periods ago |
| `-size +10M` | Larger than ten mebibyte units as defined by `find` |
| `-exec ... {} +` | Passes many matched paths safely to the command |

Avoid `find ... | xargs command` for arbitrary filenames unless null delimiters are used:

```bash
find . -type f -print0 | xargs -0 sha256sum
```

### Archives and compression

```bash
tar -cvf project.tar project/
tar -tvf project.tar
tar -xvf project.tar -C restore/
tar -czf project.tar.gz project/
tar -cJf project.tar.xz project/
```

| Letter | Meaning |
|---|---|
| `c` | Create archive |
| `t` | List archive |
| `x` | Extract archive |
| `v` | Verbose names |
| `f` | Archive filename follows |
| `z` | gzip compression |
| `J` | xz compression |

List an untrusted archive before extraction and extract into an empty disposable directory.

Individual compressors:

An **archive** collects multiple files and their names into one file, for example `tar -cf files.tar dir/`. **Compression** reduces bytes, for example `gzip files.tar` creates `files.tar.gz` and normally removes the original `.tar`. A `.gz` file is not automatically a multi-file archive. `tar -czf files.tar.gz dir/` combines archiving and gzip compression.

```bash
gzip -k file.txt
bzip2 -k file.txt
xz -k file.txt
gunzip file.txt.gz
bunzip2 file.txt.bz2
unxz file.txt.xz
```

### cpio

```bash
find project -print0 | cpio --null -ov > project.cpio
mkdir restore && cd restore
cpio -idmv < ../project.cpio
```

`cpio -o` creates an archive from a list of pathnames; `-i` extracts. `--null` pairs with `find -print0` to preserve unusual filenames.

### dd

`dd` copies blocks without understanding filesystems. A reversed `if` and `of` can destroy a disk.

Safe file example:

```bash
dd if=/dev/zero of=sample.bin bs=1M count=10 status=progress
```

| Operand | Meaning |
|---|---|
| `if=` | Input file |
| `of=` | Output file |
| `bs=1M` | Block size |
| `count=10` | Copy ten input blocks |

This creates a 10 MiB regular file. Do not substitute a block device unless the lab explicitly requires it and data loss is acceptable.

## 103.4 Streams, pipes and redirection

Every normal process starts with file descriptors:

| Descriptor | Name | Normal destination/source |
|---:|---|---|
| 0 | stdin | Keyboard/previous pipe |
| 1 | stdout | Terminal/next pipe |
| 2 | stderr | Terminal |

```bash
command > output.txt
command >> output.txt
command 2> errors.txt
command > output.txt 2>&1
command < input.txt
producer | consumer
```

- `>` creates or truncates a file before writing.
- `>>` appends.
- `2>` redirects standard error.
- `2>&1` sends descriptor 2 to the current destination of descriptor 1; ordering matters.
- `|` connects stdout of the left command to stdin of the right command.

Examples:

```bash
grep -R 'ERROR' /var/log 2>/dev/null | sort | uniq -c | sort -nr
printf '%s\n' alpha beta | tee names.txt
```

`tee` copies input to stdout and files. Use `tee -a` to append.

Command substitution captures stdout:

```bash
kernel=$(uname -r)
printf 'Kernel: %s\n' "$kernel"
```

## 103.5 Create, monitor and stop processes

A process has a PID, parent PID, credentials, environment, open files and a scheduling state. A job is the shell's view of a pipeline started from that shell.

```bash
sleep 300 &
jobs -l
fg %1
Ctrl+Z
bg %1
```

`&` starts the job in the background. `Ctrl+Z` sends a terminal stop signal; `bg` continues it in the background and `fg` brings it forward.

### View processes

```bash
ps aux
ps -ef
ps -o pid,ppid,user,stat,ni,cmd -p 1
pgrep -a sshd
top
free -h
uptime
```

`free` summarizes physical and swap memory. `uptime` reports time since boot,
logged-in user count and load averages. Load average counts runnable and
uninterruptible tasks; it is not a direct CPU-percent value.

Common state letters include `R` running/runnable, `S` interruptible sleep, `D` uninterruptible sleep, `T` stopped and `Z` zombie.

### Signals

```bash
kill -l
kill -TERM 1234
kill -KILL 1234
pkill -TERM -x process-name
killall process-name
```

SIGTERM requests orderly termination and can be handled. SIGKILL cannot be handled or ignored and prevents cleanup; use it only when graceful methods fail.

`pkill -x` requires an exact process name. Check matches first with `pgrep -a -x process-name`.

In `ps aux`, `a` includes processes with terminals belonging to other users, `u` requests a user-oriented display, and `x` includes processes without a controlling terminal. Read `USER`, `PID`, `%CPU`, `%MEM`, `STAT` and `COMMAND`; `STAT` is the state, not an error code. These BSD-style letters are used without a leading dash. `kill` sends a **signal** to a PID; despite its name, `kill -TERM` first asks a process to exit cleanly.

### Continue after logout

```bash
nohup long-command >long-command.log 2>&1 &
```

`nohup` makes the command ignore SIGHUP. Terminal multiplexers such as `screen` and `tmux` provide detachable interactive sessions and are often more convenient.

Monitor periodically:

```bash
watch -n 2 'ps -eo pid,stat,%cpu,%mem,cmd --sort=-%cpu | head'
```

## 103.6 Process priorities

The nice value normally ranges from -20 (more favorable CPU scheduling priority) to 19 (less favorable). A normally created process starts at nice value 0 and inherits changes from its parent. Nice is a scheduler hint, not a guaranteed CPU percentage.

```bash
nice -n 10 command
renice -n 15 -p 1234
ps -o pid,ni,pri,cmd -p 1234
```

An unprivileged user can normally make their processes nicer (raise the nice value) but cannot increase priority by lowering it. Root or a process with the relevant capability can request negative values.

## 103.7 Regular expressions

Globs match pathnames in the shell. Regular expressions describe text patterns for tools such as `grep` and `sed`; they are not the same language.

### Core elements

| Regex | Meaning |
|---|---|
| `^` | Start of line |
| `$` | End of line |
| `.` | Any one character |
| `[0-9]` | One character in the class |
| `[^0-9]` | One character outside the class |
| `*` | Zero or more of the previous atom |
| `+` | One or more in extended regex |
| `?` | Zero or one in extended regex |
| `{m,n}` | Repetition range in extended regex |
| `(one\|two)` | Group and alternation in extended regex |

```bash
grep '^root:' /etc/passwd
grep -E '^(error|warning):' app.log
grep -F 'literal.*text' file.txt
grep -v '^[[:space:]]*#' config.conf
```

`grep` uses basic regular expressions by default. `grep -E` uses extended expressions. `grep -F` treats patterns as fixed strings. Historical commands `egrep` and `fgrep` correspond to `grep -E` and `grep -F` but the option forms are preferred.

Read `man 7 regex` (`regex(7)`) for the local implementation's BRE/ERE
notation. In BRE, grouping and alternation commonly need backslashes, for
example `\(one\|two\)`; in ERE the equivalent is `(one|two)`.

### sed substitution and deletion

`sed` is a stream editor: it reads input line by line, applies instructions and writes output. In `s/old/new/g`, `s` means substitute, the slashes separate pattern and replacement, and `g` replaces every occurrence on a line. Without `g`, only the first match on each line changes.

```bash
printf '%s\n' 'red red' | sed 's/red/blue/g'
```

`printf` supplies one line; `|` passes it to `sed`; the quoted substitution changes both words. The result is `blue blue`. No source file is edited.

```bash
sed 's/old/new/' file.txt
sed 's/old/new/g' file.txt
sed '/^[[:space:]]*#/d' config.conf
```

These write transformed text to stdout. They do not modify the input unless an in-place option is used. Make a backup before in-place editing and remember that `sed -i` syntax varies across implementations.

## 103.8 Basic file editing with vi

Vi is modal:

| Mode | Purpose | Enter it with |
|---|---|---|
| Normal | Navigate and issue editing commands | `Esc` |
| Insert | Enter text | `i`, `a`, `o` |
| Command-line | Save, quit, search settings | `:` from Normal mode |

Open a practice file:

```bash
vi practice.txt
```

Essential Normal-mode commands:

| Command | Action |
|---|---|
| `h j k l` | Left, down, up, right |
| `w`, `b` | Next/previous word |
| `0`, `$` | Beginning/end of line |
| `gg`, `G` | First/last line |
| `x` | Delete character |
| `dd` | Delete/cut line |
| `yy` | Yank/copy line |
| `p` | Paste after cursor |
| `u` | Undo |
| `/text` | Search forward |
| `?text` | Search backward |
| `n`, `N` | Repeat search forward/backward |

Saving and exiting:

| Command | Action |
|---|---|
| `:w` | Write |
| `:q` | Quit if no unsaved changes |
| `:wq` or `ZZ` | Write and quit |
| `:q!` | Quit and discard changes |
| `:w!` | Force write when permissions and conditions permit |

Set a default editor for the current shell:

```bash
export EDITOR=vi
export VISUAL=vi
```

Other common editors include Vim, Nano and Emacs, but the objective specifically requires practical vi operation.

## Lab 103: Build a text-processing report

1. Copy `/etc/passwd` to a practice directory.
2. Select username, UID and shell fields with `cut`.
3. Sort numerically by UID.
4. Exclude comment and blank lines from a sample configuration with `grep`.
5. Count unique login shells.
6. Redirect the report and errors to separate files.
7. Verify both files with `wc`, `head` and `tail`.
8. Edit a heading into the report using vi.
9. Archive and compress the practice directory.
10. Generate a SHA-256 digest of the archive.

## Exercises

1. **103-Q1:** Contrast single and double quotes.
2. **103-Q2:** Why might `uniq` fail to remove every duplicate in an unsorted file?
3. **103-Q3:** Write a safe `find` command that prints regular `.conf` files under `/etc` changed within seven days.
4. **103-Q4:** Explain `2>&1` and why redirection order matters.
5. **103-Q5:** Contrast a shell glob and a regular expression.
6. **103-Q6:** Which signal should normally be tried before SIGKILL?
7. **103-Q7:** What is the difference between `dd`'s `if=` and `of=`?
8. **103-Q8:** In vi, delete a line, undo it, search for `server`, save and exit.

Answers are in [the answer key](../exercises/answers.md#topic-103-answers).

## Official reading

- [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [GNU Bash](https://www.gnu.org/software/bash/manual/bash.html)
- [GNU Findutils](https://www.gnu.org/software/findutils/manual/)
- [GNU Grep](https://www.gnu.org/software/grep/manual/grep.html)
- [GNU Sed](https://www.gnu.org/software/sed/manual/sed.html)
