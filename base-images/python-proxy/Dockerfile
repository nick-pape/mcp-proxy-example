# STDIO->HTTP proxy image extending python-base
FROM pape-mcp-python-base

WORKDIR /app

# Copy the stdio->HTTP proxy script
COPY proxy.py /app/proxy.py

# Default command (to be overridden in specific services)
CMD ["python", "proxy.py"]
