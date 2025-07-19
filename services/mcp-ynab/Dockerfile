FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install fastmcp uvicorn

# Install the YNAB MCP server
RUN pip install git+https://github.com/ntdef/ynab-mcp.git

# Copy proxy script
COPY proxy.py /app/proxy.py

ENV MCP_COMMAND="uv run ynab-mcp"
ENV MCP_PORT=3002

EXPOSE 3002

CMD ["python", "proxy.py"]
