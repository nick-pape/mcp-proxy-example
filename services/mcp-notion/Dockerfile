FROM node:18-slim

WORKDIR /app

# Install dependencies
RUN npm install -g @makenotion/notion-mcp-server

# Copy proxy script
COPY proxy.js /app/proxy.js
COPY package.json /app/package.json

RUN npm install

ENV MCP_COMMAND="npx @makenotion/notion-mcp-server"
ENV MCP_PORT=3003

EXPOSE 3003

CMD ["node", "proxy.js"]
