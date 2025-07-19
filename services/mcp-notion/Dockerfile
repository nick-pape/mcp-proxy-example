FROM node:18-slim

WORKDIR /app

    # Install dependencies
    RUN npm install -g @notionhq/notion-mcp-server

ENV MCP_COMMAND="npx @notionhq/notion-mcp-server"
ENV MCP_PORT=3003

EXPOSE 3003

CMD ["sh", "-c", "$MCP_COMMAND"]
