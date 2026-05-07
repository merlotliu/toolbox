# apply-prebuilt-adreno-patch

Reorganise a Qualcomm `auto-a7xbins` source drop into the nhlos prebuilt
adreno directory structure (`prebuilt_HY11/<variant>/adreno/`).

The tool builds a full copy plan first, runs a pre-copy MD5 check to show
what has changed, copies all files, then verifies every file with a
post-copy MD5 check.

## Workflow

| Step | Action |
|------|--------|
| 1 | Build copy plan (src → dst pairs, no files touched yet) |
| 2 | Pre-copy MD5 check — show files that differ or are absent |
| 3 | Copy all planned files into `<DEST_ROOT>/adreno/` |
| 4 | Post-copy MD5 check — verify every file matches source |

## Copy plan

| Source path (relative to SRC) | Destination path (relative to `adreno/`) |
|-------------------------------|------------------------------------------|
| `vendor/lib64/*.so` | `usr/lib/` |
| `vendor/lib64/pkgconfig/*.pc` | `usr/lib/pkgconfig/` |
| `vendor/firmware/*` | `usr/lib/firmware/` |
| `vendor/bin/*` | `usr/bin/` |
| `vendor/vulkan/icd.d/*` | `etc/vulkan/icd.d/` |
| `vendor/adreno/*` | `etc/adreno/` |
| `kgsl@.service`, `kgsl.service`, `adreno_test.service`, `gsl_hab_server.service` | `usr/lib/systemd/system/` |
| `kgsl@0.conf` | `usr/lib/systemd/system/sleep-notify@kgsl@0.service.d/` |
| `kgsl@1.conf` | `usr/lib/systemd/system/sleep-notify@kgsl@1.service.d/` |
| `graphics-sysusers.conf` | `usr/lib/sysusers.d/` |
| `include/c2dExt.h`, `include/gsl_profiler.h` | `usr/include/` |
| `include/private/C2D/c2d2.h` | `usr/include/` |
| `include/public/{CL,EGL,GLES,GLES2,GLES3,KHR}/` | `usr/include/{CL,EGL,…}/` |

## Usage

```
apply-prebuilt-adreno-patch [--check-only] <SRC> <DEST_ROOT>
```

## Options

| Option | Description |
|--------|-------------|
| `--check-only` | Run pre-copy MD5 check only; do not copy any files |

## Arguments

| Argument | Description |
|----------|-------------|
| `SRC` | Root of the Qualcomm `auto-a7xbins` drop |
| `DEST_ROOT` | Directory under which `adreno/` will be created (e.g. `prebuilt_HY11/sa8797/`) |

## Examples

```bash
# Dry-run: inspect what would change
apply-prebuilt-adreno-patch --check-only \
  ~/Downloads/auto-a7xbins_SA8797/auto-a7xbins \
  ~/Workspace/xref/W-8797-MASTER/nhlos/apps/apps_proc/prebuilt_HY11/sa8797

# Apply
apply-prebuilt-adreno-patch \
  ~/Downloads/auto-a7xbins_SA8797/auto-a7xbins \
  ~/Workspace/xref/W-8797-MASTER/nhlos/apps/apps_proc/prebuilt_HY11/sa8797
```
