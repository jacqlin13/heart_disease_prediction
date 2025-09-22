#!/bin/bash
# Setup script for Streamlit Cloud deployment

echo "🔧 Upgrading pip..."
python -m pip install --upgrade pip

echo "🔧 Installing dependencies..."
pip install -r requirements.txt

# Removed the unnecessary `cat /mount/admin/install_path` check
# because it caused 'No such file or directory' warnings.

echo "✅ Setup complete!"
