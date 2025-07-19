FROM pape-mcp-python-proxy

WORKDIR /app

# Install calculator MCP server (common dependencies already in base image)
RUN uv tool install mcp-server-calculator

ENV MCP_COMMAND="uvx mcp-server-calculator"
ENV MCP_PORT=3006
ENV SERVICE_NAME="Calculator MCP"

EXPOSE 3006

CMD ["python", "proxy.py"]
