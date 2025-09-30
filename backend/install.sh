#!/bin/bash

# Educational Dashboard Backend - Installation Script

echo "🚀 Installing Educational Dashboard Backend..."

# Check if Python 3.10+ is available
python_version=$(python3 --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
required_version="3.10"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.10+ is required. Found: $python_version"
    exit 1
fi

echo "✅ Python version: $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Install development dependencies
echo "🧪 Installing development dependencies..."
pip install pytest pytest-cov pytest-asyncio httpx

echo "✅ Backend installation completed!"
echo ""
echo "To start the development server:"
echo "  source venv/bin/activate"
echo "  python -m uvicorn app.main:app --reload"
echo ""
echo "To run tests:"
echo "  source venv/bin/activate"
echo "  python -m pytest tests/ -v"
