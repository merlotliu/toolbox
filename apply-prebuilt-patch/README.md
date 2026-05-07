# apply-prebuilt-patch

Apply a Qualcomm MST patch drop to the `prebuilt_HY11` directory in the
nhlos source tree.

The tool discovers every `<variant>/<target>` sub-directory inside the patch
root, compares it against the corresponding location in the destination tree,
copies changed or new files, repacks the component tar archive, and produces
a signed git commit — all in one command.

## Workflow

| Step | Action |
|------|--------|
| 1 | Extract `<target>-binaries.tar` in each destination variant directory |
| 2 | Pre-apply MD5 check — list files that differ or are new |
| 3 | Copy changed/new files from patch to destination |
| 4 | Post-apply MD5 check — verify every patch file matches destination |
| 5 | Repack `<target>-binaries.tar` from destination sub-directories |
| 6 | `git add` all changed files and tar archives |
| 7 | `git commit -s "[PATCH] update <target> libs"` |

## Usage

```
apply-prebuilt-patch -s PATCH_ROOT [-d DEST_ROOT] -t TARGET [--only-check] [-y]
```

## Options

| Option                    | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| `-s PATCH_ROOT`           | `prebuilt_HY11` directory from the MST patch drop (required) |
| `-d DEST_ROOT`            | `prebuilt_HY11` in the source tree (optional, has default)   |
| `-t TARGET`               | Component sub-directory name to match, e.g. `adreno` (required) |
| `--only-check / --check-only` | Extract tar and run pre-apply check only; do not modify anything |
| `-y / --yes`              | Skip the confirmation prompt before applying                  |

The default `DEST_ROOT` is:

```
/home/lixiang/Workspace/xref/W-8797-MASTER/nhlos/apps/apps_proc/prebuilt_HY11
```

## Examples

```bash
# Dry-run: inspect what would change for the adreno component
apply-prebuilt-patch \
  -s ~/Downloads/patch_drop/ly.au.0.1.1/apps_proc/prebuilt_HY11 \
  -t adreno \
  --only-check

# Apply the patch (will prompt for confirmation)
apply-prebuilt-patch \
  -s ~/Downloads/patch_drop/ly.au.0.1.1/apps_proc/prebuilt_HY11 \
  -t adreno

# Apply without prompt, custom destination
apply-prebuilt-patch \
  -s ~/Downloads/patch_drop/ly.au.0.1.1/apps_proc/prebuilt_HY11 \
  -d ~/Workspace/xref/R-X01-MASTER/nhlos/apps/apps_proc/prebuilt_HY11 \
  -t adreno \
  -y
```
