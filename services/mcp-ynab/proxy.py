#!/usr/bin/env python3
"""
FastMCP stdio->HTTP proxy for YNAB MCP server
"""
import os
import subprocess
import asyncio
from fastmcp import FastMCP

MCP_PORT = int(os.getenv('MCP_PORT', '3002'))

# Create FastMCP app
mcp = FastMCP("YNAB MCP")

# TODO: Implement actual proxy logic using FastMCP's proxy functionality
# For now, this is a placeholder that starts the HTTP server

if __name__ == "__main__":
    print(f"Starting YNAB MCP proxy on port {MCP_PORT}")
    mcp.run(transport="http", host="0.0.0.0", port=MCP_PORT)
