#!/bin/bash

# This script will run your Python script with a test path input.

# Ensure the correct number of arguments are provided.
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 --test_path <test_path>"
    exit 1
fi

# Parse the command-line arguments
while [[ "$#" -gt 0 ]]; do
    case "$1" in
        --test_path)
            TEST_PATH="$2"  # Get the value after --test_path
            shift 2  # Skip the next argument as it's the value for --test_path
            ;;
        *)
            echo "Unknown option $1"
            exit 1
            ;;
    esac
done

# Check if the provided test path exists
if [ ! -f "$TEST_PATH" ]; then
    echo "Error: The file '$TEST_PATH' does not exist."
    exit 1
fi

# Path to the Python script (adjust if necessary)
PYTHON_SCRIPT="./solutions/dynamic/main.py"

# Run the Python script with the provided test_path argument
python3 "$PYTHON_SCRIPT" --test_path "$TEST_PATH"
