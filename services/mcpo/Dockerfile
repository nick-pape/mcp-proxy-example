FROM pape-mcp-python-base

WORKDIR /app

# Clone MCPO and install dependencies (git, curl, uv already in base image)
RUN rm -rf /app/* && \
    git clone https://github.com/open-webui/mcpo.git . && \
    uv sync

ENV MCP_ENDPOINT=http://mcp-aggregator:3100
ENV PORT=8080

EXPOSE 8080

CMD ["uv", "run", "mcpo", "--port", "8080", "--api-key", "mcpo-secret", "--server-type", "sse", "--", "http://mcp-aggregator:3100"]
