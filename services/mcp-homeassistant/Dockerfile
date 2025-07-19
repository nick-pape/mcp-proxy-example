FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install fastmcp uvicorn requests

# Clone the HomeAssistant MCP server
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/voska/hass-mcp.git . && \
    pip install -r requirements.txt || pip install homeassistant-websocket-api

# Copy our proxy configuration
COPY proxy.py /app/proxy.py

ENV MCP_COMMAND="python main.py"
ENV MCP_PORT=3001

EXPOSE 3001

CMD ["python", "proxy.py"]
