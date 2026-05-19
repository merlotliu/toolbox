# aplog

Pull logs from an Android device via ADB, decompress `.clp`/`.clp.zst` files,
and package everything into a timestamped `.tar.gz` archive.

## Dependencies

- `adb`
- `clpd` (required only when `.clp`/`.clp.zst` files are present)

## Usage

```
aplog -s <device_id> -d <source_dir> [OPTIONS]

Required:
  -s device_id    ADB device serial number
  -d source_dir   Directory to pull from device (repeatable)

Optional:
  -n log_name     Name for the log directory and archive (default: device_id)
  -p root_dir     Root directory for output files (default: /tmp)
  -h              Show this help message
```

## Examples

```bash
# Pull two directories from a device
aplog -s 45b92d3ab0f -d /mnt/android_log -d /mnt/linux_log

# Custom name and output location
aplog -s 45b92d3ab0f -d /mnt/android_log -n VIN123456 -p ~/logs

# Pull core dumps
aplog -s 45b92d3ab0f -d /data/core -p ~/logs
```

Output files are placed under `<root_dir>/`:
- `<log_name>-<timestamp>/` — pulled log directory
- `<log_name>-<timestamp>.tar.gz` — compressed archive
