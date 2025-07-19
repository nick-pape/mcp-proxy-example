#!/usr/bin/env python3
"""
Generic FastMCP STDIO->HTTP proxy
Bridges any MCP server from STDIO transport to HTTP transport
"""
import os
import shlex
from fastmcp import FastMCP
from fastmcp.client.transports import StdioTransport

# Get configuration from environment
MCP_COMMAND = os.getenv('MCP_COMMAND', 'echo "No MCP_COMMAND specified"')
MCP_PORT = int(os.getenv('MCP_PORT', '8000'))
SERVICE_NAME = os.getenv('SERVICE_NAME', 'MCP Service')

if __name__ == "__main__":
    print(f"Starting {SERVICE_NAME} HTTP proxy on port {MCP_PORT}")
    print(f"Proxying STDIO command: {MCP_COMMAND}")
    
    # Parse the command string into command and args
    command_parts = shlex.split(MCP_COMMAND)
    
    # Create a STDIO transport for the backend MCP server
    backend_transport = StdioTransport(
        command=command_parts[0],
        args=command_parts[1:] if len(command_parts) > 1 else []
    )
    
    # Create a FastMCP proxy that bridges STDIO->HTTP
    proxy = FastMCP.as_proxy(
        backend_transport,
        name=f"{SERVICE_NAME} Proxy"
    )
    
    # Run the proxy as an HTTP server
    proxy.run(
        transport="http",
        host="0.0.0.0", 
        port=MCP_PORT
    )
