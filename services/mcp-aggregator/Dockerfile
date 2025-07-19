FROM python:3.11-slim

WORKDIR /app

# Install FastMCP
RUN pip install fastmcp uvicorn requests

# Copy aggregator script
COPY aggregator.py /app/aggregator.py

ENV MCP_PORT=3100

EXPOSE 3100

CMD ["python", "aggregator.py"]
