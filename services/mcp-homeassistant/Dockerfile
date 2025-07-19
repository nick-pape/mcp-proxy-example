FROM pape-mcp-python-base

WORKDIR /app

# Copy our proxy configuration (fastmcp, uvicorn, requests already in base image)
COPY proxy.py /app/proxy.py

ENV MCP_COMMAND="python proxy.py"
ENV MCP_PORT=3001

EXPOSE 3001

CMD ["python", "proxy.py"]
