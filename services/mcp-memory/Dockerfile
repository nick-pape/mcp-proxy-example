FROM pape-mcp-node-proxy

WORKDIR /app

# Clone the memory MCP server from the official servers repo (git already in base image)
RUN git clone https://github.com/modelcontextprotocol/servers.git && \
    cd servers/src/memory && \
    npm install && \
    npm run build

# Copy proxy script and package.json (already done in base image)
ENV MCP_COMMAND="node /app/servers/src/memory/build/index.js"
ENV MCP_PORT=3007

EXPOSE 3007

CMD ["node", "proxy.js"]
