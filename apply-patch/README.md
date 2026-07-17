# apply-patch

Apply a patch directory onto a local tree by matching relative paths.

## Usage

```bash
apply-patch -s <path/to/patch> -d <path/to/local> [--skip-new|--only-check] [-y]
```

## Options

- `-s`, `--source`: patch directory to read from
- `-d`, `--dest`: local directory to update; must be inside a git repo for apply mode
- `--skip-new`: skip files that exist in patch but not in local
- `--only-check`: compare matching relative-path files by MD5 only; do not modify anything
- `-y`, `--yes`: skip confirmation prompt before applying

## Behavior

1. Recursively scans every file under the patch directory.
2. Compares each patch file with the corresponding relative path under the local directory.
3. Prints `DIFF` for changed files and `NEW` for files absent in local.
4. In apply mode, copies changed files, runs a post-apply MD5 check, then creates a git commit.

## Example

```bash
apply-patch \
  -s /tmp/new_lib \
  -d ~/Workspace/xref/S-8295-MASTER/apps/qnx_ap/prebuilt/aarch64le/usr/lib/graphics/qc \
  --only-check
```
