# Frontend Dockerfile for Educational Dashboard
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy application code
COPY . .

# Expose port
EXPOSE 3000

# Run application in development mode
CMD ["npm", "run", "dev", "--", "--port", "3000"]

