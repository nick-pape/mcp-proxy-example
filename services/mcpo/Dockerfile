FROM python:3.11-slim

WORKDIR /app

# Install git, curl, and uv in a single RUN to combine layers
RUN apt-get update && apt-get install -y git curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    git clone https://github.com/open-webui/mcpo.git . && \
    /root/.local/bin/uv sync

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

ENV MCP_ENDPOINT=http://mcp-aggregator:3100
ENV PORT=8080

EXPOSE 8080

CMD ["uv", "run", "mcpo", "--port", "8080", "--api-key", "mcpo-secret", "--server-type", "sse", "--", "http://mcp-aggregator:3100"]
