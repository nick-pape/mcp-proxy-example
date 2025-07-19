FROM node:18-slim

WORKDIR /app

# Clone the memory MCP server from the official servers repo
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/modelcontextprotocol/servers.git && \
    cd servers/src/memory && \
    npm install && \
    npm run build

# Copy proxy script
COPY proxy.js /app/proxy.js
COPY package.json /app/package.json

RUN npm install

ENV MCP_COMMAND="node /app/servers/src/memory/build/index.js"
ENV MCP_PORT=3007

EXPOSE 3007

CMD ["node", "proxy.js"]
