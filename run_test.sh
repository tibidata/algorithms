#!/bin/bash

# Function to display usage instructions
usage() {
  echo "Usage: ./run_solution.sh --algorithm <algorithm> [--verbose <true/false>]"
  exit 1
}

# Default values for arguments
algorithm=""
verbose="true"  # Default value for verbose is true

# Static path for test cases (for 'hanoi' solution)
test_path="./tests/hanoi/test.csv"  # This is a fixed path for the test cases

# Parse named arguments using a while loop and case statement
while [[ $# -gt 0 ]]; do
  case "$1" in
    --algorithm)
      algorithm="$2"
      shift 2
      ;;
    --verbose)
      verbose="$2"  # Set verbose value to true or false
      shift 2
      ;;
    *)
      echo "Unknown option $1"
      usage
      ;;
  esac
done

# Check if the algorithm argument is provided
if [ -z "$algorithm" ]; then
  echo "Error: --algorithm is required."
  usage
fi

# Check if the 'verbose' value is valid
if [ "$verbose" != "true" ] && [ "$verbose" != "false" ]; then
  echo "Error: Invalid value for --verbose. It must be 'true' or 'false'."
  exit 1
fi

# If the solution is "hanoi", run the Python script with the static test path and verbose option
if [ "$algorithm" == "hanoi" ]; then

  # Path to the Python script you want to run
  python_script="./solutions/recursion/main.py"  # Update this to the correct path

  # Check if the Python script exists
  if [ ! -f "$python_script" ]; then
    echo "Error: Python script not found at '$python_script'"
    exit 1
  fi

  # Check if the test file exists (if it's used in the script)
  if [ ! -f "$test_path" ]; then
    echo "Error: Test file not found at '$test_path'"
    exit 1
  fi

  # Create logs directory for the specified algorithm (if it doesn't exist)
  log_directory="./logs/$algorithm"
  if [ ! -d "$log_directory" ]; then
    echo "Creating logs directory: $log_directory"
    mkdir -p "$log_directory"  # Create the directory for logs
  fi

  # Run the Python script with the test path (static) and verbose flag
  python "$python_script" --test_path "$test_path" --verbose "$verbose"

else
  echo "Error: Invalid algorithm name '$algorithm'. Only 'hanoi' is supported."
  exit 1
fi