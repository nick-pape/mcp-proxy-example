FROM pape-mcp-node-proxy

WORKDIR /app

# Clone the fetch MCP server from the official servers repo (git already in base image)
RUN git clone https://github.com/modelcontextprotocol/servers.git && \
    cd servers/src/fetch && \
    npm install && \
    npm run build

# Copy proxy script and package.json (already done in base image)
ENV MCP_COMMAND="node /app/servers/src/fetch/build/index.js"
ENV MCP_PORT=3004

EXPOSE 3004

CMD ["node", "proxy.js"]
