# MCP Fetch Service

**GitHub Repository**: [https://github.com/modelcontextprotocol/servers/tree/main/src/fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)

This is an official Model Context Protocol server that provides web content fetching capabilities. It enables LLMs to retrieve and process content from web pages, converting HTML to markdown for easier consumption by AI assistants.

## Available Tools

- `fetch` - Fetches a URL from the internet and extracts its contents as markdown
  - `url` (string, required): URL to fetch
  - `max_length` (integer, optional): Maximum number of characters to return (default: 5000)
  - `start_index` (integer, optional): Start content from this character index (default: 0)
  - `raw` (boolean, optional): Get raw content without markdown conversion (default: false)

## Available Prompts

- `fetch` - Fetch a URL and extract its contents as markdown
  - `url` (string, required): URL to fetch

## Requirements

- No authentication tokens required
- Optional: Node.js (provides more robust HTML simplifier)
- Python 3.8+ (if not using Docker)
- **Security Warning**: This server can access local/internal IP addresses - exercise caution in production environments
