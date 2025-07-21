#!/usr/bin/env python3
"""
FastMCP Aggregator - Proxies multiple MCP servers using FastMCP mounting
"""
import os
from fastmcp import FastMCP
from fastmcp.server.proxy import ProxyClient

# Get configuration from environment
MCP_PORT = int(os.getenv('MCP_PORT', '3100'))

def parse_mcp_servers():
    """Parse MCP server configuration from environment variables"""
    servers = {}
    
    # Parse from MCP_SERVERS env var (format: "name1:url1,name2:url2,...")
    servers_env = os.getenv('MCP_SERVERS', '')
    if servers_env:
        for server_config in servers_env.split(','):
            if ':' in server_config:
                name, url = server_config.strip().split(':', 1)
                servers[name.strip()] = url.strip()
    
    return servers

# MCP server endpoints
MCP_ENDPOINTS = parse_mcp_servers()

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
