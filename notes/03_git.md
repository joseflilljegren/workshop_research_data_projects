# Basic git commands

Git is a version tracking system for coding colaboration.

## How it works:

On your machine, a directory that is initiated with git is called a repository. This repository will have a `.git` folder where the version tracking data is stored. Using the git software, the code on your machine can be synched to a cloud repository (like GitHub).

Unlike DropBox or other cloud services, with `git` you have to take actions yourself. You can push your code to a cloud repository, pull code from a cloud repository, and more. When you make a change, you commit it to the cloud repository only when _you_ are done with the code.

If it is your task to fix a specific feature, you can work on it until you're ready to commit it.

### Some vocabulary:
 - **Commit**: A snapshot of the code at a specific point in time.
 - **Stage**: 
 - **Repository**: Also called a "repo". The directory that contains the `.git` folder.
 - **Push**: Send code from your local repository to a remote repository
 - **Pull**: Get code from a remote repository to your local
 - **Clone**: To pull a repo for the first time including it's current state but also its entire git-history of previous commits.

## Functioning on a per-line basis

Git operates on lines. It contains a document differentiation algorythm that calculates differences between files.

Use `diff` to check it out:

```bash
    # Look at the difference between `01_hello.py` and `01_hello_variant.py`
    diff -u 01_hello.py 01_hello_variant.py
```

In your text editor, git suppor usually marks the files and lines that are changed, new or deleted.


## How do I work with git?

For most practical use, there is a pull, edit, add, commit, push cycle.

### Pull

### Edit

### Add

### Commit

### Push

### Summary

With the commands outlined above, you can  use the most basic colaboration features.


## Claude and git

Claude can: 
 - Commit for you
 - Look through all previous iterations of code to find lost changes and revert to working version of code that you or it broke
 - Handle your version tracking and merging with other collaborators

If Claude is tasked with a specific list of changes, a named commit that describes them is a good hint to your colaborators of what _you_ have been doing - even if Claude is your only colaborator.

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


### Switching between branches


