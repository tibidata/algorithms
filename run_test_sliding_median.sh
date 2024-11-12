#!/bin/bash

# Bash script to test the Python script with --test_path argument

# Ensure the script is executed with a test file path argument
if [ -z "$1" ]; then
  echo "Usage: $0 --test_path <test_file_path>"
  exit 1
fi

# Parse the --test_path argument
while [[ "$1" =~ ^- ]]; do
  case "$1" in
    --test_path)
      TEST_PATH="$2"
      shift 2  # Skip over the argument and value
      ;;
    *)
      echo "Usage: $0 --test_path <test_file_path>"
      exit 1
      ;;
  esac
done

# Check if the test file exists
if [ ! -f "$TEST_PATH" ]; then
  echo "Error: Test file '$TEST_PATH' not found!"
  exit 1
fi

# Path to the Python script (adjust if necessary)
PYTHON_SCRIPT="./solutions/sort/main.py"

# Run the Python script with the --test_path argument
python3 "$PYTHON_SCRIPT" --test_path "$TEST_PATH"
