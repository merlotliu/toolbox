# issuefinder-tool

Command-line client for the IssueFinder API. Supports three operation modes:

- **Local processing** — upload a local log/minidump file for analysis (auto-detects tool type)
- **Cloud log download** (`--cloud-log`) — trigger a cloud log task by VIN + time and download the results
- **IssueFinder analysis** (`--issuefinder`) — run full IssueFinder analysis on a vehicle event
- **Direct download** (`--direct-download`) — download cloud logs directly without going through the IssueFinder API

## Dependencies

- Python 3

## Usage

```
issuefinder-tool [OPTIONS]

Local processing:
  -u, --upload FILE       File to upload (archives are extracted automatically)
  -t, --tool TYPE         Tool type (auto-detected if omitted)

Cloud / analysis:
  --cloud-log             Cloud log download mode
  --issuefinder           IssueFinder analysis mode
  --direct-download       Direct cloud log download mode
  --vin VIN               Vehicle VIN (required for cloud modes)
  --happen-time TIME      Issue time; formats: YYYY-MM-DDTHH:MM, "YYYY-MM-DD HH:MM",
                          "YYYY/MM/DD HH:MM", "YYYY-MM-DD HH:MM:SS"

Common options:
  --log-type TYPE         Log type for direct download (default: log_HUF_Klog)
  --time-range MINUTES    Search window around happen-time (default: 60)
  --env {prod,testtwo,ontest}  Environment (default: prod)
  --task-type ID          Flow ID for cloud log task
  --poll-interval SECS    Status polling interval (default: 30)
  --reason TEXT           Reboot reason hint
  --server URL            API server URL
  --output DIR            Output directory (default: ./results)
  --timeout SECS          Tool execution timeout (default: 300)
  --verbose               Verbose output
  --keep-env              Keep cloud environment after download
  --skip-version-check    Skip auto-update check
```

## Examples

```bash
# Auto-detect and process a local file
issuefinder-tool -u /path/to/lastlog_file

# Process a zip archive
issuefinder-tool -u /path/to/archive.zip

# Specify tool type explicitly
issuefinder-tool -t minidump_unpack -u /path/to/minidump_file

# IssueFinder analysis
issuefinder-tool --issuefinder --vin HLX33B124P1767770 --happen-time "2025-10-27 18:43"

# Cloud log download
issuefinder-tool --cloud-log --vin HLX33B124P1767770 --happen-time "2025-10-27T18:43"

# Direct download
issuefinder-tool --direct-download --vin HLX14B175S1996368 --happen-time "2025-11-06 18:00" --log-type log_HUF_Klog
```
