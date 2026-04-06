# BabelWrap MCP Server

An [MCP](https://modelcontextprotocol.io) server that gives AI agents web browsing superpowers via the [BabelWrap](https://babelwrap.com) API.

Works with Claude Desktop, Cursor, Claude Code, and any MCP-compatible client.

## Installation

```bash
# Using uvx (recommended -- no install required)
uvx babelwrap-mcp

# Using pip
pip install babelwrap-mcp

# Using pipx (isolated environment)
pipx install babelwrap-mcp
```

## Setup

### 1. Get an API Key

Sign up at [babelwrap.com](https://babelwrap.com) and create an API key from your dashboard.

### 2. Configure Your MCP Client

#### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "babelwrap": {
      "command": "uvx",
      "args": ["babelwrap-mcp"],
      "env": {
        "BABELWRAP_API_KEY": "bw_your_api_key_here"
      }
    }
  }
}
```

If you installed with `pip` or `pipx`, use the binary directly:

```json
{
  "mcpServers": {
    "babelwrap": {
      "command": "babelwrap-mcp",
      "args": [],
      "env": {
        "BABELWRAP_API_KEY": "bw_your_api_key_here"
      }
    }
  }
}
```

#### Claude Code

```bash
claude mcp add babelwrap -- uvx babelwrap-mcp
```

Then set your API key as an environment variable:
```bash
export BABELWRAP_API_KEY="bw_your_api_key_here"
```

## Available Tools

| Tool | Description |
|---|---|
| `babelwrap_new_session` | Create a new browser session |
| `babelwrap_close_session` | Close a browser session |
| `babelwrap_navigate` | Navigate to a URL |
| `babelwrap_snapshot` | Get current page state |
| `babelwrap_click` | Click an element |
| `babelwrap_fill` | Fill a form field |
| `babelwrap_submit` | Submit a form |
| `babelwrap_extract` | Extract structured data |
| `babelwrap_screenshot` | Take a screenshot |
| `babelwrap_press` | Press a keyboard key |
| `babelwrap_scroll` | Scroll the page |
| `babelwrap_hover` | Hover over an element |
| `babelwrap_upload` | Upload a file |
| `babelwrap_back` / `babelwrap_forward` | Browser history |
| `babelwrap_wait_for` | Wait for a condition |
| `babelwrap_list_pages` / `babelwrap_switch_page` | Multi-tab support |

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `BABELWRAP_API_KEY` | Yes | Your BabelWrap API key |
| `BABELWRAP_API_URL` | No | API base URL (default: `https://api.babelwrap.com/v1`) |

## Documentation

Full documentation at [babelwrap.com/docs/mcp](https://babelwrap.com/docs/mcp)

## License

MIT

<!-- mcp-name: io.github.soulfir/babelwrap-mcp -->