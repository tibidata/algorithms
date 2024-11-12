#!/bin/bash

# This script runs the graph-based solution testing Python script with a specified test data JSON file.

# Ensure that the correct number of arguments are passed.
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 --test_path <test_data_path>"
    exit 1
fi

# Parse the test data path argument
while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        --test_path)
            TEST_PATH="$2"
            shift # past argument
            shift # past value
            ;;
        *)
            echo "Invalid argument: $key"
            exit 1
            ;;
    esac
done

# Check if the specified test data file exists
if [ ! -f "$TEST_PATH" ]; then
    echo "Error: The test data file '$TEST_PATH' does not exist."
    exit 1
fi

# Path to the Python script (adjust if necessary)
PYTHON_SCRIPT="solutions/graph/main.py"

# Run the Python script with the provided test path argument
python3 "$PYTHON_SCRIPT" --test_path "$TEST_PATH"
