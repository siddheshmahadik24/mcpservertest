# MCP Streamable-HTTP Server

An experiment testing the Model Context Protocol (MCP) using the `streamable-http` transport — as opposed to the more common `stdio` transport. Includes a variant configured for deployment on an Azure VM.

## What It Does

Exposes a simple **greeting tool** via MCP:

| Tool | Input | Output |
|------|-------|--------|
| `greeting` | `name: str` | `"Hi {name}"` |

The purpose of this repo is to explore and validate MCP's streamable-http transport for use cases where stdio is not practical (e.g., remote servers, cloud VMs).

## Files

| File | Description |
|------|-------------|
| `server.py` | Local development — runs MCP with streamable-http on `localhost` |
| `server_public.py` | Azure VM variant — same transport, with notes on SSH port forwarding for external access |

## Running Locally

```bash
# Clone the repo
git clone https://github.com/siddheshmahadik24/mcpservertest.git
cd mcpservertest

# Install dependencies
uv sync

# Start the server
uv run python server.py
```

The server will be accessible at `http://127.0.0.1:8000`.

## MCP Client Config

To connect an MCP client to this running server:

```json
{
  "mcpServers": {
    "greeting-server": {
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

## Tech Stack

- **FastMCP** — MCP server framework
- **streamable-http** transport
- **uv** — package manager & runner
