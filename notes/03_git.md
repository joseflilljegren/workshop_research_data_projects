# Basic git commands

Git is a version tracking system for coding colaboration.

## How it works:

On your machine, a directory that is initiated with git is called a repository. This repository will have a `.git` folder where the version tracking data is stored. Using the git software, the code on your machine can be synched to a cloud repository (like GitHub).

Unlike DropBox or other cloud services, with `git` you have to take actions yourself. You can push your code to a cloud repository, pull code from a cloud repository, and more. When you make a change, you commit it to the cloud repository only when _you_ are done with the code.

If it is your task to fix a specific feature, you can work on it until you're ready to commit it.

### Some vocabulary:
 - **Commit**: A snapshot of the code at a specific point in time.
 - **Stage**: To mark a change as belonging in the next commit. Staged changes sit in an in-between area (the "staging area" or "index") where you assemble a commit before making it. This is what lets you commit three of the five files you touched.
 - **Repository**: Also called a "repo". The directory that contains the `.git` folder.
 - **Push**: Send code from your local repository to a remote repository
 - **Pull**: Get code from a remote repository to your local
 - **Clone**: To pull a repo for the first time including it's current state but also its entire git-history of previous commits.
 - **Remote**: The cloud copy of the repository. Yours is called `origin` by default. Check it with `git remote -v`.
 - **Branch**: A named line of development. The default one here is `master`.
 - **HEAD**: Where you are right now, meaning the commit your working files are based on.
 - **Working tree**: The actual files in your folder, as they are this second, staged or not.

The three places a change can be, in order:

```
working tree  --git add-->  staging area  --git commit-->  repository  --git push-->  remote
 (your edits)                 (selected)      (recorded)                   (shared)
```

## Functioning on a per-line basis

Git operates on lines. It contains a document differentiation algorythm that calculates differences between files.

Use `diff` to check it out:

```bash
    # Look at the difference between `01_hello.py` and `01_hello_variant.py`
    diff -u 01_hello.py 01_hello_variant.py
```

In your text editor, git suppor usually marks the files and lines that are changed, new or deleted.

Git's own version of that command compares your working tree with the last commit:

```bash
git diff            # what have I changed but not staged?
git diff --staged   # what is staged, ready to be committed?
```

Two consequences follow from working per line, and they explain most of the advice in this repo:

1. **Text files work, binary files do not.** Change one word in a `.md` file and git stores one changed line. Change one pixel in a `.png` and git stores the whole file again, with no readable diff. This is why `.gitignore` in this repo excludes images, `.xlsx`, `.docx` and zipped data.
2. **Two people can edit the same file** as long as they touch different lines. Git merges them without asking. When they touch the same lines, git stops and asks you to resolve the conflict.


## How do I work with git?

For most practical use, there is a pull, edit, add, commit, push cycle.

Before anything else, ask git where you stand. `git status` is the command you will run most often, and it tells you the branch, what is changed, what is staged, and usually what to type next.

```bash
git status
```

### Pull

Start every session by collecting what your collaborators did. This avoids the situation where you build on an outdated version and have to untangle it later.

```bash
git pull
```

If you have uncommitted edits and the pull would overwrite them, git refuses and says so. Commit your work first, then pull again.

### Edit

Work normally: edit files in your editor, or let Claude do it. Nothing is recorded yet, and nothing has left your machine. Ask git what it sees at any point:

```bash
git status          # which files are changed
git diff            # exactly which lines
```

Keep a unit of work small enough to describe in one sentence. That sentence becomes the commit message.

### Add

Staging selects which changes go into the next commit.

```bash
git add 01_hello.py            # stage one file
git add notes/                 # stage a whole folder
git add .                      # stage everything changed below the current folder
```

`git add .` is convenient and is what you will use most of the time. It is worth running `git status` first to see what you are about to include: files ignored via `.gitignore` are skipped, but a stray 400 MB download that is *not* ignored would be swept in.

To unstage something without losing the edit:

```bash
git restore --staged 01_hello.py
```

### Commit

A commit records the staged changes in your local history, with a message.

```bash
git commit -m "Add download routine for source material"
```

The message is documentation, not a formality. Conventions that pay off:

- Write in the imperative: "Add", "Fix", "Remove", not "Added" or "changes".
- Say *what and why*, not *how*. The diff already shows how.
- One logical change per commit. "Fix plot axis labels" and "add requests to requirements" are two commits, not one.

A longer explanation goes in a second paragraph: run `git commit` with no `-m` and git opens an editor for a title line, a blank line, and a body.

Nothing has been shared yet. The commit exists only on your machine.

### Push

Send your commits to the remote so others can pull them.

```bash
git push
```

If someone pushed while you were working, git rejects the push and tells you to integrate their work first. The fix is always the same: `git pull`, resolve anything that conflicts, then `git push` again.

### Summary

With the commands outlined above, you can  use the most basic colaboration features.

```bash
git pull                       # 1. get the latest
# ... edit files ...           # 2. do your work
git status                     # 3. check what changed
git add .                      # 4. stage it
git commit -m "Clear message"  # 5. record it locally
git push                       # 6. share it
```

### When something goes wrong

Git is nearly impossible to lose work with, as long as you committed. A short survival list:

```bash
# Throw away uncommitted changes to one file (cannot be undone)
git restore 01_hello.py

# See the history
git log --oneline

# Look at the project as it was at some commit, without changing anything
git show 95b8314

# Recover a single file as it was at some commit
git checkout 95b8314 -- 01_hello.py

# Undo the last commit but keep the changes in your working tree
git reset --soft HEAD~1
```

If a pull produces a **merge conflict**, git marks the disputed lines in the file with `<<<<<<<`, `=======` and `>>>>>>>`. Open the file, delete the markers, keep the text you want, then `git add` the file and `git commit`. This is also a good moment to ask Claude, which can read both sides and explain what each one was trying to do.


## Claude and git

Claude can: 
 - Commit for you
 - Look through all previous iterations of code to find lost changes and revert to working version of code that you or it broke
 - Handle your version tracking and merging with other collaborators

If Claude is tasked with a specific list of changes, a named commit that describes them is a good hint to your colaborators of what _you_ have been doing - even if Claude is your only colaborator.

In practice this means you can say things like:

- "Commit this with a message explaining what we changed and why."
- "What did we change in the last three commits?"
- "The plotting script worked yesterday and is broken now. Find the commit that broke it."
- "I pulled and got a conflict in `02_material.py`. Explain both versions before we choose."

Two habits keep this safe. **Commit before you set Claude loose on a large change**, so there is a clean point to return to. And **read the diff before you push**, because the commit carries your name whoever wrote the lines.

A list of commits is a nice way of seing how a project has evolved into its current state.

Try this:
```bash
    git log --all --decorate --oneline --graph
```

If you like the command, you can add it as an alias to your `.zshrc`:
```bash
    alias tree="git log --all --decorate --oneline --graph"
```

## Branches

A branch is a parallel line of commits. It lets you work on something unfinished without disturbing the version everybody else is using.

The default branch here is `master`, and it should always be in a state that runs. When you start something that will take more than one commit, or that might not work out, you do it on a branch and merge it back when it is ready.

```bash
git branch                      # list local branches; * marks the current one
git branch -a                   # include the remote ones
```

Branches are cheap. Creating one copies nothing and takes no time, so there is no reason to be economical with them.

### Switching between branches

```bash
# Create a new branch and move onto it
git switch -c feature/download-data

# ... edit, add, commit as usual ...

# Publish the branch the first time (later pushes are just `git push`)
git push -u origin feature/download-data

# Go back to master
git switch master

# Bring the finished work into master
git merge feature/download-data

# Delete the branch once it is merged
git branch -d feature/download-data
```

Two things to know before switching:

- **Commit first.** Uncommitted changes travel with you to the other branch, which is confusing at best. `git status` should be clean before `git switch`.
- **Branch names are documentation too.** `feature/download-data` or `fix/axis-labels` tells a collaborator what lives there; `test2` does not.

On a shared repository, the usual pattern is to push your branch and open a **pull request** on GitHub, so a collaborator reads the diff before it reaches `master`. Claude can open one for you with the `gh` command line tool, and can summarise what the branch changes.

(Older material uses `git checkout -b name` and `git checkout name`. Those still work; `git switch` is the newer, clearer spelling of the same thing.)
