#!/bin/bash

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Please install it first:"
    echo "curl -sSL https://install.python-poetry.org | python3 -"
    exit 1
fi

# Create thumbnails directory if it doesn't exist
mkdir -p thumbnails

# Install dependencies and run the thumbnail generator
echo "Installing dependencies..."
poetry install --no-interaction

echo "Generating thumbnails..."
poetry run python generate_thumbnails.py

echo "Done! Thumbnails have been generated in the 'thumbnails' directory."
echo "You can now view your website with the image grid." 