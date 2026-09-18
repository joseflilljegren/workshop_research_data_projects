# Markdown

A simple markup language that allows you to format text. This document is written in markdown. There is a guide [here](https://www.markdownguide.org/basic-syntax/), and the formal specification most tools follow is [CommonMark](https://commonmark.org/help/).

The idea is that the file stays readable as plain text. You are not hiding formatting inside a binary document; you are writing characters that a human can read in the terminal and a machine can render as a web page, a PDF or a slide deck.

## Most basic synthax and principles:

- **Bold** `**bold**`
- *Italic* `*italic*`
- **Underline** `__underline__`
- ~~Strikethrough~~ `~~strikethrough~~`
- `Inline code` `` `code` ``

Markdown is so well-spread that these even work in your Whats'App chats these days.

One caveat on the third one: in standard Markdown `__underline__` renders as **bold**, the same as `**bold**`. Markdown has no underline of its own, because underlining on a web page means "link". If you really need it, write the HTML: `<u>underline</u>`. Most Markdown renderers accept inline HTML.

The general principle: the marker wraps the text it affects, and whitespace matters. `**bold**` works, `** bold **` does not.

## Headings and lines.

A "#" marks the heading-level. Up to six levels. It is typical to leave an empty line between a heading and a paragraph.

```markdown
# Level 1: the document title, one per file
## Level 2: a section
### Level 3: a subsection
```

Use the levels in order, without skipping. Headings are not font sizes, they are structure: they become the table of contents on GitHub, the anchors in a link, and the outline that Claude uses to find the relevant part of a long file.

A line can be expressed with `---` like this:

---

The line separates the content of your file.

A hard-earned habit: paragraphs are separated by a **blank line**. A single line break is usually ignored by the renderer, so two lines of text with no blank line between them come out as one paragraph.

## Links

You can add an url to any part of your text, much like with the `<a>` tag in HTML. The synthax is `[YOUR LABEL](YOUR URL)`:

[A link to the workshop](https://github.com/joseflilljegren/workshop_research_data_projects)

Links can also point at other files in the same repository, which is how these notes refer to each other:

```markdown
[The git note](03_git.md)
[The data folder](../data/)
```

An image is the same syntax with a `!` in front. The label becomes the alt text:

```markdown
![A plot of the results](../output/figure_1.png)
```

## Lists

You can create nested, numbered and unnumbered lists with `-` like:

 - A list item
 - Another list item
   - An indented item, nested by two spaces

The items can be numbered using `n.` like:

 1. A First item
 1. A second item (it is not important which number you use)

Writing every number as `1.` is a deliberate trick: the renderer numbers them correctly anyway, and you never have to renumber the list by hand when you insert an item in the middle.

Checklists work on GitHub and in most editors, and are useful for workshop instructions and for your own project TODOs:

```markdown
- [ ] Not done yet
- [x] Done
```

## Code

Code goes in fences of three backticks. Naming the language after the opening fence turns on syntax highlighting:

````markdown
```python
def main():
    print('The workshop')
```
````

```python
def main():
    print('The workshop')
```

Use fenced code for anything a reader is meant to copy and run, and inline backticks for names of files, commands and variables inside a sentence, such as `requirements.txt` or `git status`. This is worth doing carefully in research notes: it is the difference between a reader knowing they should type something and guessing.

## Quotes and tables

A quote is a `>` at the start of the line:

> Everything that can be a text file, should be a text file.

A table is pipes and a separator row. It does not need to be aligned in the source, though it is easier to read if it is:

```markdown
| Command | What it does |
| --- | --- |
| `git status` | Show what has changed |
| `git log` | Show the history |
```

| Command | What it does |
| --- | --- |
| `git status` | Show what has changed |
| `git log` | Show the history |

## Writing and previewing

Markdown files end in `.md` and are written in any text editor. In VS Code, `Cmd+Shift+V` opens a live preview next to the file. GitHub renders any `.md` file automatically when you view it in the browser, which is why `README.md` is the front page of a repository.

## Usage

Markdown is used _everywhere_. R has an output format for Markdown. Jupyter notebooks mix markdown and python code. README files on github are often in markdown. Claude.md is a markdown file that instructs Claude how to work in a project. It is extremely machine-readable and works well with git.

That last point is the one that matters for this workshop. Git compares files line by line (see `03_git.md`). A Markdown file produces a clean, readable diff: a reviewer sees the sentence you changed. A `.docx` file is a zipped binary, so git can only report that the whole file changed, and two people editing it cannot merge their work.

The rule of thumb for a research repository:

| Purpose | Use | Not |
| --- | --- | --- |
| Notes, documentation, readme | `.md` | `.docx`, `.pages` |
| Data | `.csv` | `.xlsx` |
| Papers | `.tex` or `.md` | `.docx` |

## Further reading

- [Markdown Guide, basic syntax](https://www.markdownguide.org/basic-syntax/)
- [CommonMark reference](https://commonmark.org/help/)
- [GitHub Flavored Markdown](https://docs.github.com/en/get-started/writing-on-github) for tables, checklists and task lists
