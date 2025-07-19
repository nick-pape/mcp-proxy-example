# MCP Notion Service

**GitHub Repository**: [https://github.com/makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server)

This is the official Model Context Protocol server implementation for the Notion API. It enables AI assistants to interact with Notion workspaces, allowing them to search pages, create and update content, manage databases, and perform various operations within your Notion workspace.

## Available Tools

The server provides comprehensive access to the Notion API, including:
- **Pages & Blocks**: Create, read, update pages and block content
- **Databases**: Query and manipulate database entries
- **Search**: Find pages, databases, and content across your workspace
- **Comments**: Add comments to pages and blocks
- **Users**: Access user information and workspace members

*Note: Tools are generated dynamically from the Notion API OpenAPI specification*

## Requirements

- Notion workspace with integration access
- Notion Integration Token (get from [Notion Integrations](https://www.notion.so/profile/integrations))
- Environment variable:
  - `OPENAPI_MCP_HEADERS` - JSON string containing authorization headers:
    ```json
    {"Authorization": "Bearer ntn_****", "Notion-Version": "2022-06-28"}
    ```
- Pages/databases must be explicitly shared with your integration
- Node.js (if not using Docker)
