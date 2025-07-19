# MCP HomeAssistant Service

**GitHub Repository**: [https://github.com/voska/hass-mcp](https://github.com/voska/hass-mcp)

This is a Model Context Protocol server that enables AI assistants like Claude to interact directly with your Home Assistant instance. It allows LLMs to query device states, control smart home entities, troubleshoot automations, and create guided conversations for common home automation tasks.

## Available Tools

- `get_version` - Get the Home Assistant version
- `get_entity` - Get the state of a specific entity with optional field filtering
- `entity_action` - Perform actions on entities (turn on, off, toggle)
- `list_entities` - Get a list of entities with optional domain filtering and search
- `search_entities_tool` - Search for entities matching a query
- `domain_summary_tool` - Get a summary of a domain's entities
- `list_automations` - Get a list of all automations
- `call_service_tool` - Call any Home Assistant service
- `restart_ha` - Restart Home Assistant
- `get_history` - Get the state history of an entity
- `get_error_log` - Get the Home Assistant error log

## Requirements

- Home Assistant instance with Long-Lived Access Token
- Environment variables:
  - `HA_URL` - Your Home Assistant URL (e.g., `http://homeassistant.local:8123`)
  - `HA_TOKEN` - Your Home Assistant Long-Lived Access Token
- Python 3.13+ (if not using Docker)
