FROM pape-mcp-node-proxy

WORKDIR /app

# Install Notion MCP server
RUN npm install -g @notionhq/notion-mcp-server

ENV MCP_COMMAND="npx @notionhq/notion-mcp-server"
ENV MCP_PORT=3003

EXPOSE 3003

CMD ["node", "proxy.js"]
