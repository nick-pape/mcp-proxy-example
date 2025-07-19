FROM python:3.11-slim

WORKDIR /app

# Install dependencies including uv
RUN pip install fastmcp uvicorn && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    export PATH="/root/.local/bin:$PATH"

# Install calculator MCP server
RUN /root/.local/bin/uv tool install mcp-server-calculator

# Copy proxy script
COPY proxy.py /app/proxy.py

ENV MCP_COMMAND="uvx mcp-server-calculator"
ENV MCP_PORT=3006
ENV PATH="/root/.local/bin:$PATH"

EXPOSE 3006

CMD ["python", "proxy.py"]
