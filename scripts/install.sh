#!/bin/bash

# Simple installation script for the tool

# Function to check if a command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Check if pip is installed
if ! command_exists pip; then
    echo "pip is not installed. Please install pip first."
    exit 1
fi

# Install the packet sniffer tool
echo "Installing the packet sniffer tool..."
pip install .

echo "Installation complete. You can now run the tool using the command 'packetsniffer'."