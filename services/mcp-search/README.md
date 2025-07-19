# MCP Search Service

**GitHub Repository**: [https://github.com/mrkrsl/web-search-mcp](https://github.com/mrkrsl/web-search-mcp)

This is a TypeScript-based Model Context Protocol server that provides comprehensive web search capabilities with multiple tools for different use cases. It offers multi-engine web search that tries Google first and automatically falls back to DuckDuckGo if Google fails, plus full page content extraction from search results.

## Available Tools

- `full-web-search` - Comprehensive web search with full content extraction
  - `query` (string, required): Search query to execute
  - `limit` (integer, optional): Number of results (1-10, default: 5)
  - `includeContent` (boolean, optional): Whether to extract full page content

- `get-web-search-summaries` - Lightweight search returning only snippets/descriptions
  - `query` (string, required): Search query to execute  
  - `limit` (integer, optional): Number of results (1-10, default: 5)

- `get-single-web-page-content` - Extract content from a specific webpage
  - `url` (string, required): URL to extract content from
  - `maxContentLength` (integer, optional): Maximum content length

## Requirements

- No authentication tokens required (uses public search engines)
- Node.js 18.0.0+ and npm 8.0.0+ (if not using Docker)
- Works best with recent LLM models designed for tool use (Qwen3, Gemma 3)
- Developed and tested specifically with LM Studio
