FROM pape-mcp-python-base

WORKDIR /app

# Clone MCPO and install dependencies (git, curl, uv already in base image)
RUN rm -rf /app/* && \
    git clone https://github.com/open-webui/mcpo.git . && \
    uv sync

ENV MCP_ENDPOINT=http://mcp-aggregator:3100/mcp/
ENV PORT=8080

EXPOSE 8080

# Use streamable_http server type for HTTP MCP servers
CMD ["uv", "run", "mcpo", "--port", "8080", "--api-key", "mcpo-secret", "--server-type", "streamable_http", "--", "http://mcp-aggregator:3100/mcp/"]
