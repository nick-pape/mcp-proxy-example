# Base image for Python MCP servers with FastMCP stdio->HTTP proxy
FROM python:3.13-slim

WORKDIR /app

# Install common system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv for modern Python package management
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

# Install FastMCP and common dependencies
RUN pip install fastmcp uvicorn requests

# Copy the stdio->HTTP proxy script
COPY proxy.py /app/proxy.py

# Default command (to be overridden in specific services)
CMD ["python", "proxy.py"]
