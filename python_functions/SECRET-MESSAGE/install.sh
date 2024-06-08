#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    # Install Python
    echo "Installing Python..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    # Install pip
    echo "Installing pip..."
    sudo apt-get install -y python3-pip
fi

# Install cryptography module
echo "Installing cryptography module..."
pip3 install cryptography

echo "Installation complete."

