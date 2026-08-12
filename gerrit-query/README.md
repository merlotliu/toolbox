# gerrit-query

Query Gerrit Code Review REST API from the command line.

## Usage

```bash
gerrit-query -t <topic>              # Search by topic
gerrit-query -c <change-id>          # Get details of a specific change
gerrit-query -q <query-string>       # Raw Gerrit query
```

## Setup

```bash
gerrit-query --setup
```

Follow the prompts to enter your Gerrit cookies (GerritAccount and XSRF_TOKEN).
These are stored in `~/.config/gerrit-query/config` with restricted permissions.

### Getting cookies

1. Log in to https://gerrit.it.chehejia.com in your browser
2. Open DevTools → Application → Cookies → gerrit.it.chehejia.com
3. Copy the values for `GerritAccount` and `XSRF_TOKEN`

## Options

| Option | Description |
|--------|-------------|
| `-t, --topic <topic>` | Search changes by topic name |
| `-c, --change <id>` | Get details of a specific change (numeric ID or Change-Id) |
| `-q, --query <string>` | Arbitrary Gerrit query (overrides `-t`/`-c`) |
| `-O, --options <mask>` | Gerrit options bitmask (default: 5000081) |
| `-n, --limit <count>` | Max results (default: 25) |
| `-s, --start <index>` | Start at this result index (default: 0) |
| `-j, --raw-json` | Output raw JSON (without jq formatting) |
| `-u, --url <url>` | Gerrit server URL |
| `--setup` | Interactive cookie configuration |
| `-h, --help` | Show help |

## Examples

```bash
# Search by topic
gerrit-query -t "update_8387_qcom_baseline-ES2-AW-to-MASTER-update"

# Get change details
gerrit-query -c 12345

# Complex query
gerrit-query -q "topic:my-topic AND status:open"

# More results, raw JSON
gerrit-query -q "owner:self" -n 50 -j
```