#!/usr/bin/env python3
"""
Calculator MCP server implementation using FastMCP
"""
from fastmcp import FastMCP

# Create the calculator server
mcp = FastMCP("Calculator Server")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@mcp.tool  
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.resource("calculator://operations")
def list_operations() -> list[str]:
    """List all available calculator operations."""
    return ["add", "subtract", "multiply", "divide"]

if __name__ == "__main__":
    # Run with STDIO transport (default)
    mcp.run()
