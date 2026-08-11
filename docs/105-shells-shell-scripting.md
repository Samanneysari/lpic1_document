# Topic 105: Shells and Shell Scripting

## 105.1 Customize the shell environment

### Login and non-login shells

Bash reads different startup files depending on how it starts. A login shell represents a login session; an interactive non-login shell is commonly a terminal opened inside a desktop.

Typical Bash files:

| Scope | File | Common purpose |
|---|---|---|
| System | `/etc/profile` | System-wide login-shell environment |
| System | `/etc/bash.bashrc` on Debian family or `/etc/bashrc` on some RPM systems | System-wide interactive Bash settings |
| User | `~/.bash_profile` | Preferred user login file when present |
| User | `~/.bash_login` | Fallback login file |
| User | `~/.profile` | Further fallback, often shell-neutral |
| User | `~/.bashrc` | Interactive non-login Bash configuration |
| User | `~/.bash_logout` | Login-shell exit actions |

Bash selects the first available user login file from `.bash_profile`, `.bash_login`, and `.profile`; it does not automatically read all three. A common `.bash_profile` explicitly sources `.bashrc`:

```bash
if [ -f "$HOME/.bashrc" ]; then
    . "$HOME/.bashrc"
fi
```

`source file` and `. file` execute a file in the current shell, allowing it to change the current environment.

### PATH

```bash
case ":$PATH:" in
    *":$HOME/bin:"*) ;;
    *) PATH="$HOME/bin:$PATH" ;;
esac
export PATH
```

This adds `$HOME/bin` only when absent. Quoting prevents unwanted splitting. Avoid adding writable shared directories or `.` to privileged users' PATH because an attacker may place a misleading executable there.

### Alias and functions

```bash
alias ll='ls -alF'

mkcd() {
    mkdir -p -- "$1" && cd -- "$1"
}
```

An alias performs textual substitution suitable for short interactive shortcuts. A function accepts positional parameters and can contain shell logic.

| Item | Meaning |
|---|---|
| `$1` | First function/script argument |
| `--` | Ends option processing for supporting commands, protecting names beginning with `-` |
| `&&` | Changes directory only if creation succeeded |

Functions and aliases placed in `~/.bashrc` are normally available to new interactive Bash shells. Test after editing:

```bash
bash --noprofile --rcfile "$HOME/.bashrc" -i
```

### `/etc/skel`

Files in `/etc/skel` are templates copied when a tool creates a new home directory with skeleton processing enabled. Changes affect future accounts, not existing homes.

```bash
sudo find /etc/skel -maxdepth 2 -printf '%M %u:%g %p\n'
```

Review permissions and never place secrets or host-specific credentials in the skeleton.

### `set`, `env`, `export`, and `unset`

```bash
set | less
env | sort
export EDITOR=vi
unset EDITOR
```

`set` includes shell variables and functions and may be large. `env` shows exported environment entries. `unset` removes a variable or function in the current shell.

## 105.2 Write and customize simple scripts

### First safe script

Create `hello.sh`:

```bash
#!/usr/bin/env bash

set -o nounset

name=${1:-world}
printf 'Hello, %s\n' "$name"
```

Line by line:

| Line | Explanation |
|---|---|
| `#!/usr/bin/env bash` | Selects Bash found through `PATH`; use `#!/bin/bash` when a fixed system path is required |
| blank line | Separates interpreter declaration from logic |
| `set -o nounset` | Treats unintended use of unset variables as an error |
| `name=${1:-world}` | Uses argument 1, or `world` when unset/empty |
| `printf ... "$name"` | Prints safely as one string argument |

Make it executable and run it:

```bash
chmod 750 hello.sh
./hello.sh Alice
printf 'exit=%s\n' "$?"
```

`$?` is the exit status of the immediately preceding command. Zero conventionally means success.

### Positional parameters

| Parameter | Meaning |
|---|---|
| `$0` | Script name as invoked |
| `$1` … `$9` | Individual arguments |
| `${10}` | Argument ten; braces are required |
| `$#` | Number of arguments |
| `"$@"` | All arguments, preserving boundaries |
| `$?` | Previous command's exit status |
| `$$` | Current shell PID |

Use `"$@"` rather than unquoted `$*` when forwarding arbitrary arguments.

### Tests and conditionals

```bash
#!/usr/bin/env bash

if [ "$#" -ne 1 ]; then
    printf 'Usage: %s FILE\n' "$0" >&2
    exit 2
fi

file=$1

if [ -f "$file" ] && [ -r "$file" ]; then
    wc -l -- "$file"
else
    printf 'Error: not a readable regular file: %s\n' "$file" >&2
    exit 1
fi
```

Important tests:

| Test | Meaning |
|---|---|
| `-e path` | Path exists |
| `-f path` | Regular file |
| `-d path` | Directory |
| `-r`, `-w`, `-x` | Readable, writable, executable for current process |
| `-z string` | Empty string |
| `string1 = string2` | String equality in `[` |
| `n1 -eq n2` | Integer equality |
| `-lt`, `-le`, `-gt`, `-ge`, `-ne` | Integer comparisons |

Spaces around `[` and `]` are required because `[` is a command.

### `case`

```bash
case ${1:-} in
    start) printf 'Starting\n' ;;
    stop)  printf 'Stopping\n' ;;
    *)     printf 'Usage: %s {start|stop}\n' "$0" >&2; exit 2 ;;
esac
```

`case` compares one word with shell patterns. `;;` ends a branch.

### Loops

```bash
for file in "$@"; do
    if [ -f "$file" ]; then
        printf '%s\n' "$file"
    fi
done
```

```bash
count=1
while [ "$count" -le 3 ]; do
    printf '%s\n' "$count"
    count=$((count + 1))
done
```

`seq 1 3` is named by the objective and can generate a sequence, but shell arithmetic often avoids an external process.

### Read input

```bash
IFS= read -r line
printf 'You entered: %s\n' "$line"
```

`IFS=` preserves leading/trailing whitespace and `-r` prevents backslash interpretation.

### Command substitution and chaining

```bash
kernel=$(uname -r)
printf 'Kernel: %s\n' "$kernel"

mkdir -p backup && cp -- source.txt backup/
test -s backup/source.txt || printf 'Backup verification failed\n' >&2
```

Use `$(...)` rather than legacy backticks because it nests and quotes more clearly.

### `exec`

```bash
exec /usr/bin/logger -t example-script "script completed"
```

`exec command` replaces the shell process; statements after a successful `exec` are not executed. Redirection with `exec` can also alter the script's file descriptors.

### Exit behavior

Do not add `set -e` mechanically. Its behavior has context-dependent exceptions. Handle expected failures explicitly and test scripts. Useful strictness options include:

```bash
set -o nounset
set -o pipefail
```

`pipefail` makes a pipeline fail when an earlier command fails rather than reporting only the last command's status.

### Mail the administrator conditionally

The objective expects awareness of conditional mail. Exact MTA setup varies:

```bash
if ! backup-command; then
    printf 'Backup failed on %s\n' "$(hostname)" |
        mail -s 'Backup failure' root
fi
```

This requires a functioning local `mail` command and MTA. Do not include secrets in notification output.

### Ownership, location and SUID caution

Place local administrative scripts under a controlled location such as `/usr/local/sbin` and make them non-writable by untrusted users:

```bash
sudo install -o root -g root -m 0750 script.sh /usr/local/sbin/example-script
```

Linux normally ignores setuid bits on interpreted scripts because secure setuid-script behavior is problematic. Use `sudo` with narrowly scoped rules or a carefully designed compiled helper instead of attempting a setuid shell script.

### Validate scripts

```bash
bash -n script.sh
shellcheck script.sh
```

`bash -n` checks syntax without executing normal commands. ShellCheck is an external static-analysis tool when installed; it is not an LPIC command requirement but is excellent practice.

## Lab 105: System report script

Write a script that:

1. Requires exactly one output-directory argument.
2. Creates the directory safely.
3. Records hostname, kernel, uptime, memory and filesystem usage.
4. Sends errors to a separate log.
5. Uses a function for section headings.
6. Uses a loop for commands or files.
7. Returns a nonzero status if report creation fails.
8. Passes `bash -n` and, when available, ShellCheck.
9. Is installed with owner root and mode `0750` in a disposable lab location.

## Exercises

1. **105-Q1:** Which Bash user startup files are considered for a login shell, and are they all read automatically?
2. **105-Q2:** Contrast an alias and a function.
3. **105-Q3:** Explain why `"$@"` is important.
4. **105-Q4:** Write a condition that accepts only one readable regular file.
5. **105-Q5:** What does `pipefail` change?
6. **105-Q6:** Why is a setuid Bash script not an appropriate privilege solution?
7. **105-Q7:** What is the effect of `exec command`?

Answers are in [the answer key](../exercises/answers.md#topic-105-answers).

## Official reading

- [GNU Bash manual](https://www.gnu.org/software/bash/manual/bash.html)
- [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html)
