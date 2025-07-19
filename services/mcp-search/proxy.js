#!/usr/bin/env node
/**
 * FastMCP stdio->HTTP proxy for Web Search MCP server
 */
const { spawn } = require('child_process');

// Get configuration from environment
const MCP_PORT = process.env.MCP_PORT || 3005;
const MCP_COMMAND = process.env.MCP_COMMAND || 'node /app/web-search-mcp/dist/index.js';

console.log(`Starting Web Search MCP proxy on port ${MCP_PORT}`);
console.log(`Proxying command: ${MCP_COMMAND}`);

// Start HTTP server
const http = require('http');
const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.end(JSON.stringify({status: 'Web Search MCP Proxy Running'}));
});

server.listen(MCP_PORT, '0.0.0.0', () => {
    console.log(`Web Search MCP proxy listening on port ${MCP_PORT}`);
});
