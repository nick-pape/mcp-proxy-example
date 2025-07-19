FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install fastmcp uvicorn requests

# Copy our proxy configuration
COPY proxy.py /app/proxy.py

ENV MCP_COMMAND="python proxy.py"
ENV MCP_PORT=3001

EXPOSE 3001

CMD ["python", "proxy.py"]
