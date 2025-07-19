FROM python:3.11-slim

WORKDIR /app

# Install dependencies including uv and calculator MCP server
RUN apt-get update && apt-get install -y curl && \
    pip install fastmcp uvicorn && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    /root/.local/bin/uv tool install mcp-server-calculator && \
    rm -rf /var/lib/apt/lists/*

# Add uv to PATH permanently
ENV PATH="/root/.local/bin:$PATH"

# Copy proxy script
COPY proxy.py /app/proxy.py

ENV MCP_COMMAND="uvx mcp-server-calculator"
ENV MCP_PORT=3006

EXPOSE 3006

CMD ["python", "proxy.py"]
