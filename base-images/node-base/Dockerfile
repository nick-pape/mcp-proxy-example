# Base Node.js image with common dependencies
FROM node:18-slim

WORKDIR /app

# Install common system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

CMD ["node", "--version"]
