FROM pape-mcp-node-base

WORKDIR /app

# Clone the web search MCP server (git already in base image)
RUN git clone https://github.com/mrkrsl/web-search-mcp.git && \
    cd web-search-mcp && \
    npm install && \
    npm run build

# Copy proxy script and package.json (already done in base image)
ENV MCP_COMMAND="node /app/web-search-mcp/dist/index.js"
ENV MCP_PORT=3005

EXPOSE 3005

CMD ["node", "proxy.js"]
