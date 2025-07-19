FROM pape-mcp-python-base

WORKDIR /app

# Copy aggregator script (fastmcp, uvicorn, requests already in base image)
COPY aggregator.py /app/aggregator.py

ENV MCP_PORT=3100

EXPOSE 3100

CMD ["python", "aggregator.py"]
