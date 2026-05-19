# parse-sf-buffers

Analyze Graphics Buffer usage from a SurfaceFlinger dump.

Parses two sections from the dump:
- `GraphicBufferAllocator buffers` — system-allocated buffers (FramebufferSurface, etc.)
- `Imported gralloc buffers` — app-allocated buffers, with process names

## Dependencies

- Python 3

## Usage

```
parse-sf-buffers <dump.log> [OPTIONS]

OPTIONS:
    --by {process,layer}    Group by process (default) or layer name
    --sort {mem,count}      Sort by memory (default) or buffer count
    --top N                 Show only top N entries (0 = all)
    --csv FILE              Also write results to a CSV file
```

## Examples

```bash
# Group by process, sort by memory
parse-sf-buffers surfaceflinger.log

# Group by layer name, show top 20, sort by count
parse-sf-buffers surfaceflinger.log --by layer --top 20 --sort count

# Export to CSV
parse-sf-buffers surfaceflinger.log --csv output.csv
```
