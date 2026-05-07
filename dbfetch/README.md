# dbfetch — Daily Build Fetch

Download files from the internal Artifactory server with a single
command.  When given a directory URL, dbfetch opens an interactive browser
so you can navigate and pick the file to download.

## Dependencies

- `curl`
- `jq` (required only for directory browsing)

## Setup

```bash
bash setup           # from the toolbox root, or:
bash dbfetch/setup   # run directly
```

The setup script prompts for your Artifactory credentials and writes
them to `~/.config/dbfetch/default.conf` (mode 600).

## Usage

```
dbfetch -d <URL> [-o <output_file>]

OPTIONS:
    -d URL      Download URL (required)
    -o FILE     Output file path (default: auto-detected from URL)
    -h          Show this help message
```

**Direct file download**

```bash
dbfetch -d https://artifactory.example.com/artifactory/repo/path/to/file.zip
```

The output filename is derived from the last segment of the URL.
Use `-o` to override it.

**Interactive directory browser**

Pass a URL ending with `/` to browse the directory instead of
downloading directly:

```bash
dbfetch -d https://artifactory.example.com/artifactory/repo/path/to/dir/
```

dbfetch queries the Artifactory Storage API, lists folders and files, and
lets you navigate with numbered selections.  Enter `0` to go back,
`q` to quit.

## Configuration

Config file: `~/.config/dbfetch/default.conf`

```
LIAUTO_USERNAME=your_username
LIAUTO_PASSWORD=your_password
```

Re-run `dbfetch/setup` to update credentials.

## Uninstall

```bash
bash uninstall           # from the toolbox root, or:
bash dbfetch/uninstall   # run directly
```

Removes `~/.config/dbfetch/default.conf` and the config directory if it
is left empty.
