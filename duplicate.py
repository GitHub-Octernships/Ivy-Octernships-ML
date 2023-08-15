import os
from collections import defaultdict

def get_all_function_names(directory, startswith="test"):
    """
    Retrieves all function names from Python files in the specified directory and its subdirectories.
    
    Args:
        directory (str): Path to the directory.
        startswith (str): Prefix of the functions to extract (default is "test").

    Returns:
        list: List of all function names.
    """
    if not os.path.exists(directory):
        raise ValueError("Invalid directory")

    function_names = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path) as file_obj:
                    for line in file_obj:
                        if line.strip().startswith("def " + startswith):
                            function_name = line.strip().split("(")[0][4:]
                            function_names[directory].append(function_name)
    return function_names

def check_duplicate():
    """
    Checks for common function names across specified directories.

    Returns:
        dict: Dictionary of common function names for each directory.
    """
    core_directory = "ivy_tests/test_ivy/test_functional/test_core"
    nn_directory = "ivy_tests/test_ivy/test_functional/test_nn"
    experimental_directory = "ivy_tests/test_ivy/test_functional/test_experimental"

    function_names = {
        core_directory: get_all_function_names(core_directory),
        nn_directory: get_all_function_names(nn_directory),
        experimental_directory: get_all_function_names(experimental_directory)
    }

    common_function_names = set(function_names[core_directory]) & set(function_names[nn_directory]) & set(function_names[experimental_directory])
    return common_function_names, function_names

if __name__ == "__main__":
    common_function_names, function_names = check_duplicate()

    if common_function_names:
        print("Common functions found across directories:")
        for function_name in common_function_names:
            print(function_name)
        print("These functions already exist in the functional API.")
        exit(1)
    else:
        print("No common functions found across directories.")

  
