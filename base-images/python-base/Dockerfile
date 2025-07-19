# Base image for Python MCP servers - common dependencies only
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

# No CMD - this is just a base image
