# toolbox

Manage tools in this repository — list, install, and uninstall individual tools.

## Usage

```
toolbox OPTION [ARGS]

OPTIONS:
    --list              List all tools with installation status
    --setup             Run the repository setup script
    --install <tool>    Install a specific tool
    --uninstall <tool>  Uninstall a specific tool
    -h, --help          Show this help message
```

## Examples

```bash
# Show all tools and whether each is installed
toolbox --list

# Install a single tool
toolbox --install parse-sf-buffers

# Uninstall a single tool
toolbox --uninstall dbfetch

# Run the full repository setup (installs all tools)
toolbox --setup
```
