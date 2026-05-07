# toolbox

A collection of personal command-line tools, organized so that a single
`setup` command makes every tool available system-wide.

## Design goals

- **One repo, many tools.** Each tool lives in its own subdirectory and is
  self-contained: its executable, configuration templates, and any
  initialization logic are all kept together.

- **Zero manual PATH editing.** Running `setup` once creates symlinks in
  `~/.local/bin` for every tool, so they are available as plain commands
  after adding that directory to `PATH`.

- **Per-tool initialization.** A tool that needs first-run setup (e.g.
  creating a config file template) provides its own `setup` script.  The
  top-level `setup` discovers and invokes it automatically — no central
  registry to maintain.

- **Minimal convention, maximum discoverability.** The only hard rule is
  that a tool named `foo` lives at `foo/foo`.  Everything else (`foo/setup`,
  config templates, helper libraries) is optional and local to that
  directory.

## Repository layout

```
toolbox/
├── setup          # install all tools (run this once after cloning)
├── <tool>/
│   ├── <tool>     # main executable (must be chmod +x)
│   └── setup      # optional: first-run initialization for this tool
└── ...
```

## Getting started

**1. Clone and run setup**

```bash
git clone <repo-url> ~/Workspace/toolbox
cd ~/Workspace/toolbox
bash setup
```

**2. Add `~/.local/bin` to PATH** (if not already present)

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Open a new shell and all tools will be available directly by name.

## Adding a new tool

1. Create a directory named after the tool: `mkdir mytool`
2. Place the executable at `mytool/mytool` and make it executable:
   `chmod +x mytool/mytool`
3. Optionally add `mytool/setup` for first-run initialization.
4. Run `bash setup` from the repo root — the new tool is linked automatically.
