# Reproducable research data projects with `git` and `claude`

This workshop is tailored to research students with a basic data and coding skillset with the aim of laying a foundation for good coding and data practices borrowed from the world of data-science. More specifically:

- Feeling at home in the Terminal
- Git
- Good Claude prompting

## In preparation

To prepare for the first sessions, be sure to have the following installed and prepared on your machine.

NOTE: We're assuming that you're on a Mac for this.

### 1. Get some essential tools for your Mac:

We'll be working in the Terminal and in an Integrated Development Environment like [VS Code](https://code.visualstudio.com)  (but you can also use [Pycharm](https://www.jetbrains.com/pycharm/download/?section=mac)  or whichever IDE you're comfortable with).

A nice terminal setup on Macs is [iTerm2](https://iterm2.com/) but your existing terminal will do just fine (Search for "Terminal" on your machine). Run these in your terminal:

#### Make sure `git` is in order:

```bash
# Check whether Git is available
git --version
# If macOS asks you to install Command Line Tools, accept it.
```

#### Make sure we have homebrew:

Homebrew is a package manager for Mac. A bit like `pip` is for Python, `brew` will pull software, resolve dependencies and keep up to date software that might be indespensible for data workflows that you'd like to build in the future. You can read here about [Brew](https://brew.sh).

Check if you already have `brew`:

```bash
# Check whether brew is available
brew -v
```

If not:

- Follow the installation link on [brew.sh](https://brew.sh)
- Check that it installed correctly with `brew -v`

#### Verify a decent python version:

Python is part of Mac OS, but better versions of it may be installed using `brew`. Try this to see which version/s you have:

```bash
# Where is the python enterpreter?
which python

# What's the python version?
python --version

# Do yo have a python distribution installed with brew as `python3`
which python3
python3 --version
```

We'll be using a virtual environment into which we install any python packages that our projects will require. Vanilla Python is very capable, but packages like `pandas` for example, needs to be installed to be used. Sinice packages are essentially adding, and may work differently alongside eachother in different versions, or have different versions on different machines, shared data projects typically have setups that the same or similar code is ran when code is pulled to different machines. We'll achieve this with a virtual environment, and you can [look at this video](https://www.youtube.com/watch?v=G9_FNnApn_E) which explains the basics.

This repo comes with a `requirements.txt` so you'll be able to install all the nessecary packages with one line as soon as you've pulled the repo and set up git appropriately.



#### 2. A github account:

Go to [https://github.com](https://github.com) and create your account. Make it look like your name. Be aware that the name might be part of your public image for decades. Please remember your **GitHub username**. It is the username shown on your GitHub profile, not necessarily your email address.

Once you have created your account, send your GitHub username to `josef.lilljegren@rug.nl` so that you can be added as a collaborator on the repo in question.



#### 3. Set up `git` on your Mac

Git needs to know _who_'s making commits from your machine.

Set up the following by using the EMAIL ADRESS of your github account:

```bash
# Global git setup on your machine: Provide your name and email
git config --global user.name "Your Name";
git config --global user.email "your-email@example.com";
```

You can always check your setup with `git config --global --list`.

We'll be using git from the terminal, but there are both visual tools or plugins for VS Code that you'd might want to look in to later.



#### 4. Pull the workshop repo to your machine

The repo of this workshop is at: `https://github.com/joseflilljegren/workshop_research_data_projects`

Choose a place on _your_ computer where you would like to keep the workshop materials. For example, you might use your Documents folder. Some people have a central Repo's folder in `~/Repos`, while others have repos spread out in their respective projects. You should never have a GitHub repository _inside_ another one though. Assuming you choose to work with the workshop from `~/Documents`, do this to clone the workshop directory:

```bash
# Go to your Documents / Target folder:
cd ~/Documents;

# Clone the repo:
git clone https://github.com/joseflilljegren/workshop_research_data_projects.git;

# Move into the repo and check it out
cd workshop_research_data_projects;
ls -la;
open .;
```

If you're in VS Code, `code .` will open the workshop project in VS Code.



#### 5. Get a Claude subscription

We'll be using Claude as a coding agent. You'd need a paid subscription which your university may (or may not) generously provide for you.

The Claude agent should run in your Terminal, which is nice, but requires `Node.js`.

To get Node.js and Clade Code running, do this:

```bash
# Check if you already have Node:
node --version
# This should print a version like v18.x, v20.x, or v22.x
# If not, you can install it using `brew`
brew install node

# Install Claude Code using Nodes:
npm install -g @anthropic-ai/claude-code

# Check that it went well:
claude --version
```

The first time you envoke Claude Code on your machine, it will take you to the anthropic site to authenticate your Claude subscription. This only needs to be done once.

In the workshop we'll make some config to the Claude on your system to try to sandbox it a bit for security and integrity reasons.



#### 6. Stand by to be accesped as a collaborator to the workshop

Once you're added to the workshop directory, you'll be able to make changes and push them to the repository. This we will explore together during the workshop.


## Checklist:

Have I:
 - [ ] Installed git (`git -v`)
 - [ ] Got a user on github for which I remember my email and username
 - [ ] Pulled/cloned the workshop directory to my machine (maybe at ~/Documents/workshop_research_data_projects)
 - [ ] Installed a coding editor / IDE like VS Code
 - [ ] Installed `brew`
 - [ ] Installed Claude Code (via Node)
 - [ ] Gotten a Claude subscription so I can use `claude` in the terminal
