# Base image for Node.js MCP servers with FastMCP stdio->HTTP proxy
FROM node:18-slim

WORKDIR /app

# Install common system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install FastMCP globally (version 2.0.0+)
RUN npm install -g fastmcp@^2.0.0

# Copy the stdio->HTTP proxy script
COPY proxy.js /app/proxy.js
COPY package.json /app/package.json

RUN npm install

# Default command (to be overridden in specific services)
CMD ["node", "proxy.js"]
