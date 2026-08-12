# veh-platform

Query a vehicle's platform/chip (e.g. `SS2`/`SS3`/`SS4`) by VIN, using the
internal `ssp-vcs-service` vehicle-info API.

## Dependencies

- `curl`
- `jq` (required for the default summary output; raw output with `-r` works without it)

## Setup

```bash
bash setup                  # from the toolbox root, or:
bash veh-platform/setup     # run directly
```

The setup script prompts for the `x-chj-gwtoken` (gateway auth token, copied
from a logged-in browser session request against
`ssp-vehcloud-web.prod.k8s.chehejia.com`) and writes it to
`~/.config/veh-platform/default.conf` (mode 600).

> Note: this token appears to be short-lived / session-bound. If queries
> start failing, re-capture a fresh token from the browser and re-run setup.

## Usage

```
veh-platform -v <VIN> [OPTIONS]

OPTIONS:
    -v VIN    Vehicle VIN to query (required)
    -r        Print full raw JSON response instead of just the platform summary
    -h        Show this help message
```

```bash
veh-platform -v HLX33B120T2705626
# VIN:            HLX33B120T2705626
# series:         理想L7
# vehProject:     X03C
# hardPlatform:   SS31PRO
# vehPlatform:    SS3.0|SS3.1
# variableModel:  ...

veh-platform -v HLX33B120T2705626 -r   # full raw JSON
```

`vehPlatform` values map to chip platforms as follows:

| vehPlatform | 芯片/平台 |
|---|---|
| `SS2.x` | SS2 / 8155 |
| `SS3.x` | SS3 / 8295 |
| `SS4.x` | SS4 / 8797 |

## Configuration

Config file: `~/.config/veh-platform/default.conf`

```
CHJ_GWTOKEN=<token>
```

Re-run `veh-platform/setup` to update the token.

## Uninstall

```bash
bash uninstall               # from the toolbox root, or:
bash veh-platform/uninstall  # run directly
```

Removes `~/.config/veh-platform/default.conf` and the config directory.
