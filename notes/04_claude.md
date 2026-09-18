# Claude

Claude is a large language model made by Anthropic. **Claude Code** is the version of it that runs as a program in your terminal, inside a project folder, with the ability to act rather than only answer.

The difference from a chat window is the whole point. A chat window gives you text to copy. Claude Code reads your actual files, edits them, runs your code, reads the error message, fixes it, runs your git commands and installs your packages. You stay in charge by approving the actions it proposes.

For research work that makes it a capable but literal-minded collaborator: excellent at the mechanical parts of a data project, dependent on you for what the project is actually trying to find out.


## Claude in the terminal

We use claude code by envoking it in the terminal. The terminal application will auto-educate you by showing tips.

Start it from inside the project, with the virtual environment active (see `01_setup.md`):

```bash
cd ~/Documents/workshop_research_data_projects
source .venv/bin/activate
claude
```

The folder you start it in matters. That is the folder it can see.

Useful things to know at the prompt:

| Keystroke | Effect |
| --- | --- |
| `Esc` | Interrupt Claude mid-answer |
| `Esc` twice | Go back and edit an earlier message |
| `Shift+Tab` | Cycle permission modes, including planning mode |
| `@` | Reference a file by name, with completion |
| `!` | Run a shell command yourself; the output goes into the conversation |
| `#` | Save an instruction to memory (`CLAUDE.md`) |
| `Ctrl+C` twice | Quit |

### Commands:

Prefixed by `/`, you can see claude's commands with `/help`. Check your `/usage` to know your subscriptio quotas. 

Some other usefull commands are:

 - `/init` — read the project and generate a `CLAUDE.md` for it
 - `/clear` — start a fresh conversation, forgetting the current one. Use it whenever you switch task; a long, unrelated history makes answers worse
 - `/context` — see how full the context window is
 - `/compact` — summarise the conversation so far to free up room
 - `/model` — switch model
 - `/permissions` — see and edit what Claude is allowed to do without asking
 - `/config` — general settings
 - `/resume` — reopen an earlier conversation
 - `/review` — have Claude review the changes on your branch
 - `/help` — the full list, which is longer than this one

### Claude.md

The `CLAUDE.md` file reads into context every time you task Claude Code with a mission. It is supposed to be consice and informative of the project and its environment. Look at the `CLAUDE.md` for this project or launch claude in some coding project of your own and envoke `/init` for Claude to summarise and generate the `CLAUDE.md` for you.

What belongs in it is whatever a new collaborator would need told to them on day one and would not find by reading the code:

- What the project is and what the folders are for
- How to run things here (activate `.venv`, run with `python`, install with `pip install -r requirements.txt`)
- Conventions you want followed: docstring style, where output goes, what must never be committed
- Anything Claude has got wrong twice. Write the correction down instead of repeating it

Keep it short. It is loaded into every single request, so a bloated `CLAUDE.md` costs you context on every turn and gets skimmed rather than followed. A page is plenty.

`CLAUDE.md` is committed to git, so it is shared with the people who clone the repo, and its history shows how the project's conventions evolved.

### Setup:

Claude can be information greathy. On your system, using it's commandline powers, it can alter preferences and read your credentials. 

Treat it as you would a capable new research assistant with a terminal: trustworthy for the work, but not someone you hand your password manager to. Two mechanisms control this.

**Permission modes**, cycled with `Shift+Tab`:

- *Default*: Claude asks before editing files or running commands
- *Accept edits*: file edits go through without asking, commands still ask
- *Plan mode*: Claude may read and investigate but may not change anything

**Permission rules**, in a settings file, which apply always and are not a per-prompt decision. Project settings live in `.claude/settings.json` inside the repo, and your personal settings in `~/.claude/settings.json`.

Forbit Claude to read from `.env`:

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./**/secrets/**)"
    ],
    "allow": [
      "Bash(git status)",
      "Bash(git diff:*)",
      "Bash(python:*)"
    ]
  }
}
```

`deny` wins over everything: those files are unreadable to Claude even if you ask it to read them. `allow` is the opposite convenience, listing commands so routine that being asked about them is noise. You can edit these interactively with `/permissions` instead of by hand.

Worth knowing about this repo: `.gitignore` currently ignores `.claude`, so these settings stay on your machine. If you want the whole workshop group to share one set of rules, unignore `.claude/settings.json` and commit it, keeping `.claude/settings.local.json` ignored for personal overrides.

Sensible defaults for a research project:

- Deny reads of `.env`, credential files and anything with a key in it
- Never put a real secret in a file Claude reads. `.env` holds the secret, `.env.example` holds the names with fake values, and only the example is committed
- Be careful with `--dangerously-skip-permissions`. It exists, it is occasionally useful in a throwaway container, and it is the wrong default on the laptop holding your research data
- Keep git underneath everything. A committed project is one where any mistake is a `git restore` away

### Planning mode:

Planning mode is the mode where Claude can look but not touch. It reads files, greps, runs read-only commands and then writes out a plan for your approval. Nothing is edited until you accept it.

Enter it with `Shift+Tab` until the prompt shows plan mode.

Use it whenever the task is bigger than a one-liner or you are not yet sure what you want. The plan is the cheap place to find out that Claude misunderstood the task: reading a plan takes a minute, reviewing a diff across nine files takes considerably longer. It is also useful when you are new to a codebase, since "explain how this works and plan the change" gets you both things at once.

The plan is a proposal, not a contract. Edit it, argue with it, remove the steps you disagree with, then let it run.

### Skills:

A skill is a folder of instructions that Claude loads when it becomes relevant. It turns a procedure you would otherwise retype every time into something the project simply knows: how to build a figure to your lab's house style, how to validate a dataset before analysis, how to format a citation.

A skill is a folder with a `SKILL.md` in it, placed either in the project (`.claude/skills/`) or in your personal folder (`~/.claude/skills/`) if you want it everywhere. Run `/help` to see what is currently available.

#### Build your own skill

```
.claude/skills/
└── clean-survey-data/
    └── SKILL.md
```

`SKILL.md` is Markdown with a short frontmatter block at the top:

```markdown
---
name: clean-survey-data
description: Clean and validate raw survey exports from the Qualtrics dump. Use when working with files in source_material/surveys/.
---

# Cleaning survey data

1. Read the raw CSV with `pandas.read_csv(..., dtype=str)` so IDs keep leading zeros.
2. Drop responses where `consent != "yes"`.
3. Normalise column names to snake_case.
4. Write the result to `data/clean/` and never overwrite the raw file.

Report how many rows were dropped and why.
```

The `description` is the important line: it is how Claude decides whether the skill applies to what you just asked. Write it to say both *what it does* and *when to use it*.

A skill lives in the repo, so it is version tracked and shared. It is the difference between a method that exists in one person's head and a method the whole group follows.

#### Download a skill

Skills and other extensions are distributed as plugins, from a marketplace:

```
/plugin marketplace add <owner/repo>
/plugin install <name>
```

You can also install one by hand: a skill is only a folder, so copying it into `.claude/skills/` works.

Read a skill before you install it. It is a set of instructions you are handing to something with access to your files, and the same judgement applies as to any code you run from the internet.


## Prompting

The general shape of a good prompt here is: **context, task, constraints, expected output.** "Using the CSV in `data/`, produce a figure of response rate by faculty, saved as PNG in `output/`, using matplotlib only" beats "make me a plot", and it beats it by more the larger the project gets.

A few things that consistently help:

- **Point at files.** `@02_material.py` is unambiguous; "the download script" makes Claude go looking
- **Say what not to do.** "Do not touch `01_hello.py`" and "do not install anything new" are cheap and effective
- **Ask for a plan when the task is vague.** See planning mode above
- **Work in small steps and commit between them.** A reviewable diff is worth more than an impressive one
- **Start a new conversation when you change topic.** `/clear` costs nothing and stale context degrades answers
- **Correct it in the file, not in the chat.** If you find yourself giving the same instruction a third time, it belongs in `CLAUDE.md`

And the one that matters most in research: **Claude is confident whether or not it is right.** It will happily write a plausible statistical justification for the wrong test. Verification stays with you. Ask it to show the numbers, run the code, print the intermediate result.

### Specifically ask Claude to use your commandline tools

Claude can handle git, but also anything you'd install using pip or brew. In this repo, we make use of `image magick`.

This is worth being explicit about, because Claude will otherwise reach for the tool it knows rather than the one you installed. Naming it steers the work:

- "Use ImageMagick to convert every TIFF in `source_material/` to PNG at 1200px wide, into `output/`"
- "Use `pandas`, not the `csv` module, and keep the IDs as strings"
- "Use the `gh` command to open a pull request for this branch"
- "Run this with the project's `.venv`, not the system Python"

Every tool you install with `brew` or `pip` becomes a capability the agent can use. Installing `imagemagick` did not just give *you* an image converter, it gave your assistant one.

### Study the output of claude's work

You'll see that it executes commands on your system to read preferences and code files.

Read those lines rather than scrolling past them. They tell you which files it opened, which commands it ran and what came back, which is how you learn both what Claude is doing and, often, how the tool itself works. A good deal of terminal fluency can be picked up this way.

Two checks before anything becomes permanent:

```bash
git diff            # read what actually changed, line by line
git status          # check nothing unexpected is staged
```

The commit goes out under your name. Claude wrote the lines, you are the author of the work.
