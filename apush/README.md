# apush

Push Android build artifacts to a device via `adb`, driven by an INI-style
config file (`apush.conf`) that maps named sections to lists of
`local-file -> remote-path` pairs.

## Usage

```
apush [-s serial] [-l] [-L section] section1 [section2 ...]
```

## Options

| Option       | Description                                      |
|--------------|--------------------------------------------------|
| `-s serial`  | Specify adb device serial                        |
| `-l`         | List all sections defined in `apush.conf`        |
| `-L section` | Show files in a section without pushing          |
| `-h`         | Show help                                        |

## Environment

| Variable         | Description                                          |
|------------------|------------------------------------------------------|
| `APUSH_BASE_PATH`| Root of the build output (required for push mode)    |

## Config file

The config is stored at `~/.config/apush/apush.conf` and is created
automatically from the bundled template when you run `./setup` from the
repo root.  Edit it to add your own sections.

The format is a simple INI style.  Each section groups the files that
belong to one logical component.  Each line inside a section is:

```
<relative-local-path>    <absolute-remote-path>
```

The local path is relative to `$APUSH_BASE_PATH`.

```ini
[surfaceflinger]
system/bin/surfaceflinger          /system/bin/surfaceflinger
system/lib64/libgui.so             /system/lib64/libgui.so

[gralloc]
vendor/lib64/hw/gralloc.default.so /vendor/lib64/hw/gralloc.default.so
```

## Examples

```bash
# set build root
export APUSH_BASE_PATH=~/Workspace/xref/R-X01/android/out/target/product/HU_SS2MAXF

# push one or more sections
apush surfaceflinger
apush surfaceflinger gralloc

# target a specific device
apush -s 192.168.1.100:5555 surfaceflinger

# inspect the config
apush -l              # list all sections
apush -L surfaceflinger   # preview files without pushing
```
