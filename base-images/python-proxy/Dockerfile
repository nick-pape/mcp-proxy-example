# Base image for Python MCP servers with FastMCP stdio->HTTP proxy
FROM python:3.11-slim

WORKDIR /app

# Install FastMCP and common dependencies
RUN pip install fastmcp uvicorn

# Copy the stdio->HTTP proxy script
COPY proxy.py /app/proxy.py

# Default command (to be overridden in specific services)
CMD ["python", "proxy.py"]
