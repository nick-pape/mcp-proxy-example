FROM pape-mcp-python-proxy

WORKDIR /app

# Install the YNAB MCP server (git already in base image)
RUN pip install git+https://github.com/ntdef/ynab-mcp.git

ENV MCP_COMMAND="uv run ynab-mcp"
ENV MCP_PORT=3002
ENV SERVICE_NAME="YNAB MCP"

EXPOSE 3002

CMD ["python", "proxy.py"]
