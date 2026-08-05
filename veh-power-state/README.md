# veh-power-state

Query a VIN's `powermanager.powerstate-event.report` events (Android +
Linux power-state transitions) over a time range, via the DIP
`dip-data-msg-parsing-service` `veh-event` API.

## Dependencies

- `curl`
- `jq`

## Setup

```bash
bash setup           # from the toolbox root, or:
bash veh-power-state/setup
```

Prompts for a Bearer token and saves it to `~/.config/veh-power-state/config`
(mode 600). Grab the token from a browser's DevTools Network tab while
logged in to id.lixiang.com and hitting the CFE offline-data-web page that
calls this API (`Authorization: Bearer ...` header). **The token is
short-lived (~1h)** — re-run setup whenever requests start failing.

## Usage

```
veh-power-state -v <VIN> (-d <YYYY-MM-DD> | -s <START> -e <END>) [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `-v VIN` | Vehicle VIN (required) |
| `-d DATE` | Query the whole day (`YYYY-MM-DD`) |
| `-s START` / `-e END` | Custom time window (`"YYYY-MM-DD HH:MM:SS"`) |
| `--side SIDE` | Filter: `android` \| `linux` \| `all` (default `all`) |
| `--json` | Print raw event list as JSON instead of a table |
| `-h` | Show help |

## Examples

```bash
veh-power-state -v HLX33B16XT1322818 -d 2026-08-05
veh-power-state -v HLX33B16XT1322818 -s "2026-08-05 14:00:00" -e "2026-08-05 15:30:00"
veh-power-state -v HLX33B16XT1322818 -d 2026-08-05 --side android
veh-power-state -v HLX33B16XT1322818 -d 2026-08-05 --json
```
