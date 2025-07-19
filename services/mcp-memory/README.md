# MCP Memory Service

**GitHub Repository**: [https://github.com/modelcontextprotocol/servers/tree/main/src/memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)

This is an official Model Context Protocol server that provides persistent memory capabilities using a local knowledge graph. It enables AI assistants to remember information about users across chat sessions by storing entities, relationships, and observations in a structured graph format.

## Available Tools

### Graph Management
- `create_entities` - Create multiple new entities in the knowledge graph
- `create_relations` - Create multiple new relations between entities  
- `delete_entities` - Remove entities and their associated relations
- `delete_relations` - Remove specific relations from the graph

### Data Management
- `add_observations` - Add new observations to existing entities
- `delete_observations` - Remove specific observations from entities

### Query & Retrieval
- `read_graph` - Read the entire knowledge graph structure
- `search_nodes` - Search for nodes based on query across entity names, types, and observations
- `open_nodes` - Retrieve specific nodes by name

## Requirements

- No authentication tokens required
- Optional environment variable:
  - `MEMORY_FILE_PATH` - Custom path for memory storage JSON file (default: `memory.json`)
- Node.js (if not using Docker)
- Local file system access for persistent storage
