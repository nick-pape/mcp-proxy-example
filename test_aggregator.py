#!/usr/bin/env python3
"""
Test script to manually verify the aggregator is working properly
"""
import asyncio
from fastmcp import Client

async def test_calculator():
    # Connect to the calculator HTTP server
    client = Client("http://mcp-calculator:3006/")
    
    try:
        async with client as c:
            print("🎯 Testing Calculator MCP Proxy Connection...")
            
            # 1. Test basic connectivity
            try:
                await c.ping()
                print("✅ Server ping successful - connection established!")
            except Exception as e:
                print(f"❌ Ping failed: {e}")
                return
            
            # 2. List available tools
            try:
                tools = await c.list_tools()
                print(f"✅ Found {len(tools.tools)} tools:")
                for tool in tools.tools:
                    print(f"   - {tool.name}: {tool.description}")
            except Exception as e:
                print(f"⚠️  Failed to list tools: {e}")
            
            # 3. List available resources
            try:
                resources = await c.list_resources()
                print(f"✅ Found {len(resources.resources)} resources:")
                for resource in resources.resources:
                    print(f"   - {resource.uri}: {resource.description}")
            except Exception as e:
                print(f"⚠️  Failed to list resources: {e}")
            
            # 4. Test calculator-specific functionality if any tools are available
            if len(tools.tools) > 0:
                try:
                    # Try to call the first available tool with empty params
                    first_tool = tools.tools[0]
                    print(f"🔧 Testing tool: {first_tool.name}")
                    result = await c.call_tool(first_tool.name, {})
                    print(f"✅ Tool result: {result.content[0].text if result.content else str(result.data)}")
                except Exception as e:
                    print(f"⚠️  Failed to call tool {first_tool.name}: {e}")
                
            print("🎉 Calculator proxy test completed!")
            
    except Exception as e:
        print(f"❌ Failed to connect to calculator proxy: {e}")

if __name__ == "__main__":
    print("🚀 Starting manual calculator proxy test...")
    asyncio.run(test_calculator())
