FROM node:18-slim

WORKDIR /app

# Install dependencies and clone the web search MCP server
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/mrkrsl/web-search-mcp.git && \
    cd web-search-mcp && \
    npm install && \
    npm run build

# Copy proxy script
COPY proxy.js /app/proxy.js
COPY package.json /app/package.json

RUN npm install

ENV MCP_COMMAND="node /app/web-search-mcp/dist/index.js"
ENV MCP_PORT=3005

EXPOSE 3005

CMD ["node", "proxy.js"]
