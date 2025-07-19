FROM pape-mcp-python-base

WORKDIR /app

# Install calculator MCP server (common dependencies already in base image)
RUN uv tool install mcp-server-calculator

# Copy proxy script
COPY proxy.py /app/proxy.py

ENV MCP_COMMAND="uvx mcp-server-calculator"
ENV MCP_PORT=3006

EXPOSE 3006

CMD ["python", "proxy.py"]
