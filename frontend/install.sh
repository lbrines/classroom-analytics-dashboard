#!/bin/bash

# Educational Dashboard Frontend - Installation Script

echo "🚀 Installing Educational Dashboard Frontend..."

# Check if Node.js is available
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed."
    echo "Please install Node.js 18+ from https://nodejs.org/"
    exit 1
fi

# Check Node.js version
node_version=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
required_version="18"

if [ "$node_version" -lt "$required_version" ]; then
    echo "❌ Node.js 18+ is required. Found: v$(node --version | cut -d'v' -f2)"
    exit 1
fi

echo "✅ Node.js version: $(node --version)"

# Check if npm is available
if ! command -v npm &> /dev/null; then
    echo "❌ npm is required but not installed."
    exit 1
fi

echo "✅ npm version: $(npm --version)"

# Install dependencies
echo "📚 Installing dependencies..."
npm install

echo "✅ Frontend installation completed!"
echo ""
echo "To start the development server:"
echo "  npm run dev"
echo ""
echo "To build for production:"
echo "  npm run build"
echo ""
echo "To run tests:"
echo "  npm run test"
echo ""
echo "The frontend will be available at http://localhost:3000"
