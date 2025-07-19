#!/bin/bash

# Build script for MCP aggregation setup

echo "Building MCP Aggregation Stack..."

# Copy environment template if .env doesn't exist
if [ ! -f .env ]; then
    echo "Copying .env.template to .env - please update with your actual values!"
    cp .env.template .env
fi

# Build all services
echo "Building Docker services..."
docker-compose build

echo "Build complete!"
echo ""
echo "Next steps:"
echo "1. Update .env file with your actual API keys and tokens"
echo "2. Run: docker-compose up -d"
echo "3. Access the OpenAI-compatible endpoint at: http://localhost:8080"
echo ""
echo "Individual MCP endpoints (for testing):"
echo "- HomeAssistant: http://localhost:3001"
echo "- YNAB: http://localhost:3002"
echo "- Notion: http://localhost:3003"
echo "- Fetch: http://localhost:3004"
echo "- Search: http://localhost:3005"
echo "- Calculator: http://localhost:3006"
echo "- Memory: http://localhost:3007"
echo "- Aggregator: http://localhost:3100"
