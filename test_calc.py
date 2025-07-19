#!/usr/bin/env python3

import asyncio
from fastmcp import Client

async def test_calculator():
    """Test the calculator MCP server"""
    
    client = Client("http://localhost:8001/mcp/")
    
    try:
        async with client:
            print("✅ Connected to calculator MCP server")
            
            # Test ping
            await client.ping()
            print("✅ Ping successful")
            
            # List tools
            tools = await client.list_tools()
            print(f"✅ Available tools: {[tool.name for tool in tools]}")
            
            # Test a calculation if tools are available
            if tools:
                tool_name = tools[0].name
                print(f"🧮 Testing tool: {tool_name}")
                
                # Try to call the first tool with some test parameters
                # Note: actual parameters depend on the calculator implementation
                result = await client.call_tool(tool_name, {"expression": "2 + 2"})
                print(f"✅ Calculation result: {result}")
                
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_calculator())
