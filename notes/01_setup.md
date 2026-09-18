# Setup

This workshop runs Claude Code in the terminal for python examples which run in a virtual environment.

## To get back in:

Initiate the virtual environment in the project folder. Every working session starts with the same three lines, in this order:

```bash
# 1. Go to the project (adjust the path to where you cloned it)
cd ~/Documents/workshop_research_data_projects

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Start Claude Code
claude
```

When the environment is active, your prompt is prefixed with `(.venv)`:

```
(.venv) josef@macbook workshop_research_data_projects %
```

That prefix is the only reliable sign. If it is missing, `python` and `pip` point at the system Python and anything you install lands in the wrong place.

To leave it again, type `deactivate`, or just close the terminal window. The environment is active per terminal tab, not per machine, so a new tab needs `source .venv/bin/activate` again.

**First time only**, the environment has to be built before it can be activated:

```bash
cd ~/Documents/workshop_research_data_projects
python3 -m venv .venv                     # create it
source .venv/bin/activate                 # activate it
python -m pip install --upgrade pip       # update the installer
pip install -r requirements.txt           # install the project's packages
```


## What is a Virtual Environment?

A folder inside your project that holds its own Python interpreter and its own installed packages. Here it is called `.venv`.

Without it, every `pip install` goes into one shared system-wide Python. Project A needs `pandas` 1.5, project B needs 2.2, and one of them breaks. With it, each project gets its own sealed box and they never meet.

Three properties worth remembering:

- **It is disposable.** Nothing you care about lives in `.venv`. If it breaks, delete the folder and rebuild it from `requirements.txt`.
- **It is not committed.** `.venv/` is listed in `.gitignore`. It contains thousands of machine-specific binary files, which is exactly what git is bad at.
- **It is rebuilt, not copied.** Your collaborator does not receive your environment. They receive `requirements.txt` and build an equivalent one.

Check which interpreter you are really using at any time:

```bash
which python
# .../workshop_research_data_projects/.venv/bin/python   <- good
# /usr/bin/python3                                       <- NOT active
```

If it all goes wrong, throw it away and start over. This is safe:

```bash
deactivate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## What is `git`?

A version tracking system. It records snapshots of your project over time and lets several people change the same files without overwriting each other.

A folder that git is tracking is called a **repository**, and the history lives in a hidden `.git` folder inside it. Your machine holds a complete copy of that history; GitHub holds another copy that you and your collaborators sync against by pushing and pulling.

Unlike Dropbox, nothing syncs automatically. You decide what gets recorded and when, and you attach a message saying what the change was for. That deliberate step is the point: the history becomes a readable account of how the project got to its current state.

See `03_git.md` for the commands.


## What is Claude Code?

Claude Code is Anthropic's coding agent, run as a program in your terminal with the command `claude`.

It is not a chat window with a copy button. It runs inside your project folder and can read your files, write to them, run terminal commands, run your code, and use git. You describe what you want in plain language; it proposes and carries out the steps, asking permission before actions that change things.

Two consequences follow, and both matter for research work:

- Because it acts on your real files, you want git underneath it. Git is the undo button that makes it safe to let an agent edit your project.
- Because it reads your files to do its job, it can read files you would rather it did not. Configuring what it may and may not touch is part of setup, not an afterthought.

See `04_claude.md`.


## What is Python?

The programming language the examples are written in. macOS already ships a copy, which is there for the operating system's own use rather than yours, so we install our own with `brew` and then isolate each project's packages in a virtual environment.

Note the naming trap on macOS: outside a virtual environment the command is `python3` (plain `python` may not exist). Inside an activated `.venv`, `python` works and means the environment's interpreter.

```bash
python3 --version   # which Python is on the machine
which python3       # where it lives
```

Run the workshop examples with the environment active:

```bash
python 01_hello.py
python 02_material.py
```


## What is `pip`?

Python's package installer. It fetches libraries such as `pandas` or `requests` from the Python Package Index and installs them into whichever environment is currently active. This is why activating first is not optional.

```bash
pip install requests           # install a package into the active environment
pip list                       # what is installed right now
pip freeze > requirements.txt  # write the exact versions to the manifest
pip install -r requirements.txt  # rebuild an environment from that manifest
```

`requirements.txt` is a plain text file and it **is** committed to git. It is the contract between your laptop and everybody else's. Whenever you add a package, re-run `pip freeze > requirements.txt` and commit it, so the next person to clone the repo gets the same versions you used.


## What is `brew`?

Homebrew is a package manager for macOS. Where `pip` installs Python libraries, `brew` installs whole programs: Python itself, Node.js, command line utilities, databases.

```bash
brew -v                 # check it is installed
brew install <name>     # install a program
brew list               # what you have installed
brew update             # refresh brew's catalogue
brew upgrade            # update installed programs
```

Installing tools this way rather than by downloading installers means the tool can be reinstalled by a single documented command, which makes your setup something you can write down and hand to someone else.


### Installing a cool tool with brew: `image magick`

ImageMagick is a command line toolkit for images: convert formats, resize, crop, read metadata, process a thousand files in one loop. It is a good example of a tool with no graphical interface at all, which is precisely what makes it usable from a script or by Claude.

```bash
brew install imagemagick

# Check it worked
magick -version
```

A few things it does:

```bash
# Convert a file to another format
magick input.tiff output.png

# Resize to 800px wide, keeping the aspect ratio
magick input.jpg -resize 800x output.jpg

# Inspect an image without opening it
magick identify -verbose scan.jpg

# Convert every TIFF in source_material into a PNG in output
magick mogrify -format png -path output source_material/*.tiff
```

The point for this workshop: once a tool like this is installed, you can tell Claude "use ImageMagick to downscale every scan in `source_material/` into `output/`" and it will write and run the command. Tools you install are capabilities you hand to the agent.
