# MCP Aggregation Stack

This Docker Compose setup creates a comprehensive MCP (Model Context Protocol) server aggregation system that exposes multiple MCP servers through a single OpenAI-compatible endpoint.

**Note:** This setup now includes all your key requested MCP servers: HomeAssistant, YNAB, Notion, Fetch, Search, Calculator, and Memory (using the official knowledge graph-based persistent memory system).

## Architecture

```
Individual MCP Servers (Docker containers)
├── HomeAssistant MCP (Python stdio → HTTP)
├── YNAB MCP (FastMCP HTTP)  
├── Notion MCP (Python stdio → HTTP)
├── Fetch MCP (Node.js stdio → HTTP)
├── Search MCP (Python stdio → HTTP)
└── Calculator MCP (Python stdio → HTTP)
                    ↓
            FastMCP Aggregator
        (Combines all MCP servers)
                    ↓
                  MCPO
        (OpenAI tool server wrapper)
                    ↓
              OWUI/Clients
```

## Services

### Individual MCP Servers
Each MCP server runs in its own isolated container:

- **mcp-homeassistant** (Port 3001): Home Assistant integration using [voska/hass-mcp](https://github.com/voska/hass-mcp)
- **mcp-ynab** (Port 3002): YNAB (You Need A Budget) integration using [ntdef/ynab-mcp](https://github.com/ntdef/ynab-mcp)
- **mcp-notion** (Port 3003): Notion workspace integration using [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server)
- **mcp-fetch** (Port 3004): Web content fetching from [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)
- **mcp-search** (Port 3005): Web search functionality using [mrkrsl/web-search-mcp](https://github.com/mrkrsl/web-search-mcp)
- **mcp-calculator** (Port 3006): Mathematical calculations using [githejie/mcp-server-calculator](https://github.com/githejie/mcp-server-calculator)
- **mcp-memory** (Port 3007): Knowledge graph-based persistent memory using [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)

### Aggregation Layer
- **mcp-aggregator** (Port 3100): FastMCP instance that combines all individual MCPs
- **mcpo** (Port 8080): MCPO wrapper providing OpenAI-compatible API

## Setup

1. **Clone and configure:**
   ```bash
   # Windows
   build.bat
   
   # Linux/Mac
   ./build.sh
   ```

2. **Update environment variables:**
   Edit `.env` file with your actual API keys and tokens:
   ```env
   HASS_URL=http://your-homeassistant:8123
   HASS_TOKEN=your_token
   YNAB_TOKEN=your_ynab_token
   NOTION_TOKEN=your_notion_token
   SEARCH_API_KEY=your_search_key
   ```

3. **Start the stack:**
   ```bash
   docker-compose up -d
   ```

4. **Access the API:**
   - OpenAI-compatible endpoint: `http://localhost:8080`
   - Individual MCPs: `http://localhost:300X` (where X is 1-6)
   - Aggregator: `http://localhost:3100`

## Usage

The main endpoint at `localhost:8080` provides an OpenAI-compatible tool server that can be used with OWUI or any other OpenAI-compatible client.

## Development

### Adding New MCP Servers

1. Create a new service directory: `services/mcp-newserver/`
2. Add Dockerfile and any proxy scripts needed
3. Update `docker-compose.yml` with the new service
4. Update the aggregator configuration to include the new endpoint

### Base Images

- `base-images/python-proxy/`: For Python stdio MCP servers
- `base-images/node-proxy/`: For Node.js stdio MCP servers

## Notes

- Each MCP runs in isolation for security and environment separation
- All stdio-based MCPs are wrapped with FastMCP to provide HTTP endpoints
- Only the final MCPO endpoint (port 8080) needs to be exposed publicly
- Internal communication happens over Docker network

## Troubleshooting

### Individual MCP Health Checks
- Check individual MCP health: `curl http://localhost:300X/health` (where X is 1-6)
- View logs: `docker-compose logs mcp-servicename`
- Restart specific service: `docker-compose restart mcp-servicename`

### Common Issues

**Port Conflicts:**
- If ports 3001-3006 or 8080 are in use, update `docker-compose.yml` to use different ports
- Make sure to update the aggregator environment variables accordingly

**API Token Issues:**
- HomeAssistant: Create a Long-Lived Access Token in Home Assistant
- YNAB: Get your API token from [YNAB Developer Settings](https://app.ynab.com/settings/developer)
- Notion: Create an integration at [Notion Integrations](https://www.notion.so/profile/integrations)

**Build Failures:**
- Ensure Docker has sufficient resources (4GB+ RAM recommended)
- Some servers require internet access during build to clone repositories
- Check Docker logs: `docker-compose logs --tail=50 service-name`

### FastMCP Proxy Status
Note: The current proxy implementations are placeholders. For full functionality, they need to implement actual FastMCP stdio→HTTP proxying. This is a known limitation that requires additional development.
