FROM python:3.11-slim

WORKDIR /app

# Install git and clone MCPO
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/open-webui/mcpo.git . && \
    pip install -r requirements.txt

ENV MCP_ENDPOINT=http://mcp-aggregator:3100
ENV PORT=8080

EXPOSE 8080

CMD ["python", "main.py"]
