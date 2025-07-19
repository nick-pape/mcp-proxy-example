#!/usr/bin/env python3
"""
FastMCP Aggregator - Proxies multiple MCP servers using FastMCP mounting
"""
import os
from fastmcp import FastMCP
from fastmcp.server.proxy import ProxyClient

# Get configuration from environment
MCP_PORT = int(os.getenv('MCP_PORT', '3100'))

# MCP server endpoints
MCP_ENDPOINTS = {
    #'homeassistant': os.getenv('HOMEASSISTANT_URL', 'http://mcp-homeassistant:3001/mcp'),
    #'ynab': os.getenv('YNAB_URL', 'http://mcp-ynab:3002/mcp'),
    #'notion': os.getenv('NOTION_URL', 'http://mcp-notion:3003/mcp'),
    #'fetch': os.getenv('FETCH_URL', 'http://mcp-fetch:3004/mcp'),
    #'search': os.getenv('SEARCH_URL', 'http://mcp-search:3005/mcp'),
    'calculator': os.getenv('CALCULATOR_URL', 'http://mcp-calculator:3006/mcp'),
    #'memory': os.getenv('MEMORY_URL', 'http://mcp-memory:3007/mcp'),
}

# Create main FastMCP aggregator server
mcp = FastMCP("MCP Aggregator")

@mcp.tool()
def list_available_servers():
    """List all available MCP servers and their endpoints"""
    return {
        "servers": list(MCP_ENDPOINTS.keys()),
        "endpoints": MCP_ENDPOINTS,
        "note": "All server tools are available with prefixes: homeassistant_, ynab_, notion_, etc."
    }

def setup_mcp_proxies():
    """Setup and mount MCP proxy servers for each backend service"""
    print(f"Setting up MCP proxies for {len(MCP_ENDPOINTS)} services...")
    
    for service_name, endpoint_url in MCP_ENDPOINTS.items():
        try:
            print(f"Creating proxy for {service_name} -> {endpoint_url}")
            
            # Create a proxy for each MCP server endpoint
            proxy = FastMCP.as_proxy(
                ProxyClient(endpoint_url),
                name=f"{service_name.title()} Proxy"
            )
            
            # Mount the proxy with the service name as prefix
            # This will make tools available as: {service_name}_{tool_name}
            mcp.mount(proxy, prefix=service_name)
            
            print(f"✓ Mounted {service_name} proxy with prefix '{service_name}_'")
            
        except Exception as e:
            print(f"✗ Failed to setup proxy for {service_name}: {e}")

# Setup all proxies
setup_mcp_proxies()

if __name__ == "__main__":
    print(f"Starting MCP Aggregator on port {MCP_PORT}")
    print(f"Available MCP servers: {list(MCP_ENDPOINTS.keys())}")
    print("All server tools will be available with service name prefixes")
    print("Example: homeassistant_get_state, ynab_get_accounts, etc.")
    
    # Use FastMCP's HTTP transport
    mcp.run(transport="http", host="0.0.0.0", port=MCP_PORT)
