# fdb — Fast Download from Build

Download files from the internal Artifactory server with a single
command.  When given a directory URL, fdb opens an interactive browser
so you can navigate and pick the file to download.

## Dependencies

- `curl`
- `jq` (required only for directory browsing)

## Setup

```bash
bash setup        # from the toolbox root, or:
bash fdb/setup    # run directly
```

The setup script prompts for your Artifactory credentials and writes
them to `~/.config/fdb/default.conf` (mode 600).

## Usage

```
fdb -d <URL> [-o <output_file>]

OPTIONS:
    -d URL      Download URL (required)
    -o FILE     Output file path (default: auto-detected from URL)
    -h          Show this help message
```

**Direct file download**

```bash
fdb -d https://artifactory.example.com/artifactory/repo/path/to/file.zip
```

The output filename is derived from the last segment of the URL.
Use `-o` to override it.

**Interactive directory browser**

Pass a URL ending with `/` to browse the directory instead of
downloading directly:

```bash
fdb -d https://artifactory.example.com/artifactory/repo/path/to/dir/
```

fdb queries the Artifactory Storage API, lists folders and files, and
lets you navigate with numbered selections.  Enter `0` to go back,
`q` to quit.

## Configuration

Config file: `~/.config/fdb/default.conf`

```
LIAUTO_USERNAME=your_username
LIAUTO_PASSWORD=your_password
```

Re-run `fdb/setup` to update credentials.

## Uninstall

```bash
bash uninstall        # from the toolbox root, or:
bash fdb/uninstall    # run directly
```

Removes `~/.config/fdb/default.conf` and the config directory if it
is left empty.
