#!/usr/bin/env python3
"""
FastMCP Aggregator - Combines multiple MCP servers
"""
import os
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse, JSONResponse

# Get configuration from environment
MCP_PORT = int(os.getenv('MCP_PORT', '3100'))

# MCP server endpoints
MCP_ENDPOINTS = {
    'homeassistant': os.getenv('HOMEASSISTANT_URL', 'http://mcp-homeassistant:3001'),
    'ynab': os.getenv('YNAB_URL', 'http://mcp-ynab:3002'),
    'notion': os.getenv('NOTION_URL', 'http://mcp-notion:3003'),
    'fetch': os.getenv('FETCH_URL', 'http://mcp-fetch:3004'),
    'search': os.getenv('SEARCH_URL', 'http://mcp-search:3005'),
    'calculator': os.getenv('CALCULATOR_URL', 'http://mcp-calculator:3006'),
    'memory': os.getenv('MEMORY_URL', 'http://mcp-memory:3007'),
}

# Create main FastMCP app
mcp = FastMCP("MCP Aggregator")

# TODO: Use FastMCP's proxy/mount functionality to combine all servers
# See: https://gofastmcp.com/servers/proxy#multi-server-configurations

@mcp.tool()
def list_available_servers():
    """List all available MCP servers"""
    return {
        "servers": list(MCP_ENDPOINTS.keys()),
        "endpoints": MCP_ENDPOINTS
    }

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    """Health check endpoint"""
    return PlainTextResponse("OK")

@mcp.custom_route("/info", methods=["GET"])
async def server_info(request: Request) -> JSONResponse:
    """Server information endpoint"""
    return JSONResponse({
        "name": "MCP Aggregator",
        "servers": list(MCP_ENDPOINTS.keys()),
        "endpoints": MCP_ENDPOINTS,
        "mcp_path": "/mcp/"
    })

if __name__ == "__main__":
    print(f"Starting MCP Aggregator on port {MCP_PORT}")
    print(f"Available MCP servers: {list(MCP_ENDPOINTS.keys())}")
    
    # Use mcp.run() with http transport for web service
    mcp.run(transport="http", host="0.0.0.0", port=MCP_PORT)
