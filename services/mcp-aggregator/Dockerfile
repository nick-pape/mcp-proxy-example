FROM pape-mcp-python-base

WORKDIR /app

# Copy aggregator script (fastmcp, uvicorn, requests already in base image)
COPY aggregator.py /app/aggregator.py

# Default configuration
ENV MCP_PORT=3100

# MCP Server Configuration
# Use CSV format: "name1:url1,name2:url2,..."
# Server URLs and ports should be configured in docker-compose.yml
# Available servers: homeassistant, ynab, notion, fetch, search, calculator, memory
ENV MCP_SERVERS=""

EXPOSE 3100

CMD ["python", "aggregator.py"]
