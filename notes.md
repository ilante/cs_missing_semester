# 1 Course overview + the shell

## Bourne Again SHell - BASH

Textual computer interface. 

* Whats the difference between shell and terminal?

* `$` - you are not root user
* You can type any *command* that is then interpreted by the shell

Below we execute the `echo` *command* with *arguments*.
```
ila@spacebar ~ % cd cs_missing_semester
ila@spacebar cs_missing_semester % echo hello
hello
ila@spacebar cs_missing_semester % echo "hello world"
hello world
ila@spacebar cs_missing_semester % echo hello \world
hello world
```

```
ila@spacebar cs_missing_semester % date
Wed Mar 16 12:32:42 CET 2022
```
The shell will execute all comands matching any of its programming keywords. If you use a term that does not match the shell (lets say `hmmbuild`), it consults the *environment variable* called `$PATH`.

* `$PATH` lists the directories the shell should search for programs.
* Colon seperated lists  

```
ila@spacebar cs_missing_semester % echo $PATH
/Users/ila/opt/anaconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin
```
### Navigating the shell

* What is a path on the shell?
  * A delimited list of directories separated by / (L,M) and \ (W)
  * On linux and mac the path \ is the 'root' of the fs
    * All directories and files lie under this root  
  * In windows on the other hand, there is one root for each disk partition 
    * E.g. `C:\`)
* Absolute path: starts with `\`
* Relative path: relative to wd (`pwd` 'print working directory')

```
ila@spacebar cs_missing_semester % pwd 
/Users/ila/cs_missing_semester
```

Spechial directories:
* `.` curr dir
* `..` par dir

Move to prev dir
```
cd -
```
* Difference between `flags` and `options`?
  * Anything that does not take a value is a flag

First pos indicates filetype:
`-` regular file
`d` directory!
`l` symbolic link: reference to another file
`c` character device
`b` block device

```
ila@spacebar /dev/sdt % ll
total 0
brw-r-----  1 root  operator         1,   0 Mar 16 11:23 disk0
brw-r-----  1 root  operator         1,   1 Mar 16 11:23 disk0s1
brw-r-----  1 root  operator         1,   2 Mar 16 11:23 disk0s2
brw-r-----  1 root  operator         1,   3 Mar 16 11:23 disk1
brw-r-----  1 root  operator         1,   4 Mar 16 11:23 disk1s1
brw-r-----  1 root  operator         1,   7 Mar 16 11:23 disk1s2
brw-r-----  1 root  operator         1,   8 Mar 16 11:23 disk1s3
brw-r-----  1 root  operator         1,   6 Mar 16 11:23 disk1s4
brw-r-----  1 root  operator         1,   5 Mar 16 11:23 disk1s5
crw-rw-rw-  1 root  wheel           24,  16 Mar 16 11:23 dtrace
```

```
ila@spacebar cs_missing_semester % ll ..
total 912
-rw-r--r--   1 ila  staff   608B Aug 12  2021 013
drwxrwxrwx   9 ila  staff   288B Mar  4 09:52 01_irst
drwxr-xr-x   5 ila  staff   160B Dec 16 15:49 01_unibo
```

### Permissions:

owner - group - every one else

`rwx`

* If you dont have `w` on a dir you cant delete files
* E.g. if you have `w` on a file in a dir for which you do not have `w` you cannot delete the file. But you could delete the content of the file.

`rmdir` only for empty dirs (should use).

## Connecting programs

* two primary 'streams'
  * input
  * output
  
* We use `<` and `>` to redirect streams:
  
```
ila@spacebar cs_missing_semester % cat < README
# [CS Missing Semester](https://missing.csail.mit.edu/2020/)

Contains my notes and exercises.

* All videolectures are [here](https://www.youtube.com/playlist?list=PLyzOVJj3bHQuloKGG59rS43e29ro7I57J)
```

* `|` take output of prog1 to prog2


## Root

`sudo` - 'do as super user'
`sudo su` - 'super user do; shell as super user'

```
-s, --shell Run the shell specified by the SHELL environment variable if it is set or the
                   shell specified by the invoking user's password database entry.  If a command is
                   specified, it is passed to the shell for execution via the shell's -c option.  If
                   no command is specified, an interactive shell is executed.  Note that most shells
                   behave differently when a command is specified as compared to an interactive
                   session; consult the shell's manual for details.
```

todo tee cmd
todo exercizes

# Shell Tools and Scripting

* Difference between:
```
source mcd.sh

# and

bash mcd.sh
```
* `$?`  
* $!!
* $_ `previous`

* Why not echo "$date" but "$(date)"?


# Vim

* Customize and stick with it! 
    * Takes about 20 hrs in the new editor until your back to normal speed

* Vim emulators are available in many other editors and including your browser

* Vim is 'modal'
    * normal 
    * insert 
    * replace
    * visual
        * line shift v
        * block control 
    * command-line

Ways to express shortcuts:
    * ctrl+V &rarr; ^V &rarr; <C-V>

* `hjkl` 
* `8j` 8 lines down

## Commands

* `:help :w` gives me the help pages at section `:w`
* leave `help` using `:q`
* you can split the screen to see 2 parts of the same file
* `:q` quit's current window
    * That way you can close the current split screen

## Normal mode 
* The vim interface **IS** a programming language
* vim allows you to tipe at your thinking speed

* `w` word
* `b` back one word
* `e` end of word 
* 0 beginning of line
* `^` first **non-empty** char in line
* `$` end of line
* `^d` down by page
* `^u` up by page
* `G` end of buffer
* `gg`
* `^m` middle
* `^h` highest 
* `^l` lowest
* `de`delete the end of a word 
* `r` takes another character as argument and replaces: Lemi
* `u` undo
* `^r` redo
* `y` yank `yy` copy entire line
* `yw` yank word

## Chunks

* `v` visual line
* `^v` visual block
* `d[]()i`

* `jj.` didnt produce expected result

# 4. Data Wrangling

`ssh tsp journalctl | sshd > tsp.log` 

## SED

Anchoring: match `^` beginning or `$` end of line...

`(match whats in the parenthesis)`

regex101.com

`sort -nk1,1` numeric, white space seperated column

## AWK 

Column-based editor. Parses based on whitespace seperated cols

# 6. [Version Control (Git)](https://missing.csail.mit.edu/2020/version-control/)

![xkcd git](https://imgs.xkcd.com/comics/git.png)

`git log --all --graph --decorate`

## Snapshots

* Git models the history of blobs (files) and trees (directories)
* A 'tree' maps names to blobs or trees that it contains

E.g.:

```
<root> (tree)
|
+- foo (tree)
|  |
|  + bar.txt (blob, contents = "hello world")
|
+- baz.txt (blob, contents = "git is wonderful")
```

* Top level tree `<root>` holds to elements: 'foo' which itself contains the blob 'bar.txt.'

## Modelling history: relating snapshots called commits

* History is a Directed Acyclic Graph (DAG) of snapshots called commits.
    * Each snapshot in Git refers to a set of parents (preceding snapshots).
    * Why a set of parents?
        * Because a snapshot migt bescent from mulitple parents, e.g. due to merging two parallel branches of development.

* each `o` represents a commit such that the history can be represented like below:
* Each arrow points toward the parent of each commit in a 'comes before' relation
```
o <-- o <-- o <-- o
            ^
             \
              --- o <-- o
```
* After the third commit, the history branches into two separated branches
    * This can be useful when developing a new feature while fixing a bug independently from each other
    * The separated branches can be merged in the future:

```
o <-- o <-- o <-- o <---- o
            ^            /
             \          v
              --- o <-- o
```
* Commits are immutable!
* While mistakes can be corrected, while all **edits**  to the commit history are creating **new commits**

## Git's data model in pseudocode

A simple model of history:
```
# a file is a bunch of bytes
type blob = array<byte>

# a directory contains named files and directories
type tree = map<string, tree | blob>

# a commit has parents, metadata, and the tob-level tree
type commit = struct { 
    parents: array<commit>
    author: string
    message: string
    snapshot: tree
}
```

## Objects and content-addressing

An 'object' is a blob, a tree or a commit:


## Merging 


On the example of `animal.py` 

* First branch `main` (yup lets be PC)
* Second branch `cat` changing script to add 'cat functionality'
* Third branch `dog` changegin script to add `dog functionality`

```
i@cs_missing_semester %      git log --all --graph --decorate --oneline
*   f2e837e (HEAD -> main) Merge branch 'dog'
|\
| * 71a852e (dog) add dog functionality
* | dedfded (cat) add cat functionality
|/
```

* Above we can see how branches `dog` and `cat` are parent sof the commit `f2e837e` bing` HEAD` pointing to `main`.

