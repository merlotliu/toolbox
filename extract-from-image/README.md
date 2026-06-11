# extract-from-image

Extract a file by name from Android/Linux firmware images without requiring
root or external tools. Supported formats:

| Format | Notes |
|--------|-------|
| erofs | Pure Python parser — no dependencies |
| ext4 (raw) | Requires `debugfs` |
| Android sparse (wrapping ext4) | Requires `debugfs` |

## Usage

```
extract-from-image -t <target> [-d <dir>] [-i <image>] [-o <output_dir>]
```

## Options

| Option | Description |
|--------|-------------|
| `-t`   | Filename to extract, e.g. `libGSLKernel.so` |
| `-d`   | Directory to search for image files |
| `-i`   | Specific image file (skips interactive selection) |
| `-o`   | Output directory (default: current directory) |
| `--no-prescan` | Skip binary pre-scan (slower but thorough) |

## Workflow

1. **Scan** — binary pre-scan over every candidate image to find which ones
   contain the target filename string
2. **Select** — if multiple images match, an interactive prompt lets you pick
   one, several (`1,3`), or all (`a`)
3. **Extract** — walks the filesystem inside the chosen image(s), follows
   symlinks, and writes the file to the output directory

## Examples

```bash
# Search all images in a directory, choose interactively
extract-from-image -t libGSLKernel.so -d ./images

# Extract from a specific image into ~/Downloads
extract-from-image -t libGSLKernel.so -i machine-image-sa8797.erofs -o ~/Downloads

# Extract a binary from all images at once (skip interactive prompt)
extract-from-image -t vendor_service -d ./images --no-prescan
```
