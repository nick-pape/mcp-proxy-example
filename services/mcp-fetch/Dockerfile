FROM node:18-slim

WORKDIR /app

# Clone the fetch MCP server from the official servers repo
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/modelcontextprotocol/servers.git && \
    cd servers/src/fetch && \
    npm install && \
    npm run build

# Copy proxy script
COPY proxy.js /app/proxy.js
COPY package.json /app/package.json

RUN npm install

ENV MCP_COMMAND="node /app/servers/src/fetch/build/index.js"
ENV MCP_PORT=3004

EXPOSE 3004

CMD ["node", "proxy.js"]
