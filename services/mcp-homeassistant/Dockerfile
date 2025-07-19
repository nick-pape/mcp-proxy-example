FROM pape-mcp-python-proxy

WORKDIR /app

# Install HomeAssistant MCP server 
RUN pip install git+https://github.com/voska/hass-mcp.git

ENV MCP_COMMAND="python -m hass_mcp"
ENV MCP_PORT=3001
ENV SERVICE_NAME="HomeAssistant MCP"

EXPOSE 3001

CMD ["python", "proxy.py"]
