#!/bin/bash
set -e

# Create venv if not exists
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Activate venv
source .venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers if Playwright is in requirements
python -c "import sys; import pkgutil; sys.exit(0 if pkgutil.find_loader('playwright') else 1)" \
  && playwright install || true

echo "✅ Environment ready."
