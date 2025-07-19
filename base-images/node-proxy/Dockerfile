# Base image for Node.js MCP servers with FastMCP stdio->HTTP proxy
FROM node:18-slim

WORKDIR /app

# Install FastMCP and dependencies
RUN npm install -g fastmcp

# Copy the stdio->HTTP proxy script
COPY proxy.js /app/proxy.js
COPY package.json /app/package.json

RUN npm install

# Default command (to be overridden in specific services)
CMD ["node", "proxy.js"]
