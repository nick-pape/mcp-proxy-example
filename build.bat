@echo off

REM Build script for MCP aggregation setup (Windows)

echo Building MCP Aggregation Stack...

REM Copy environment template if .env doesn't exist
if not exist .env (
    echo Copying .env.template to .env - please update with your actual values!
    copy .env.template .env
)

REM Check if user wants development mode
set /p DEV_MODE=Build in development mode? (y/N): 
if /i "%DEV_MODE%"=="y" (
    echo Building development services...
    docker-compose -f docker-compose.dev.yml build
) else (
    echo Building all services...
    docker-compose build
)

echo Build complete!
echo.
echo Next steps:
echo 1. Update .env file with your actual API keys and tokens
if /i "%DEV_MODE%"=="y" (
    echo 2. Run: docker-compose -f docker-compose.dev.yml up -d
    echo 3. Test endpoints: Calculator: http://localhost:3006, Fetch: http://localhost:3004
) else (
    echo 2. Run: docker-compose up -d
    echo 3. Access the OpenAI-compatible endpoint at: http://localhost:8080
)
echo.
echo Individual MCP endpoints for testing:
echo - HomeAssistant: http://localhost:3001
echo - YNAB: http://localhost:3002
echo - Notion: http://localhost:3003
echo - Fetch: http://localhost:3004
echo - Search: http://localhost:3005
echo - Calculator: http://localhost:3006
echo - Memory: http://localhost:3007
echo - Aggregator: http://localhost:3100
