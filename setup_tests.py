import sys
from run_tests_CLI.get_all_tests import BACKENDS

def write_to_file(filename, content):
    """
    Writes the provided content to the specified file.
    
    Args:
        filename (str): Name of the file to write to.
        content (str): Content to write to the file.
    """
    with open(filename, "w") as file:
        file.write(content)

def main():
    if len(sys.argv) < 2:
        return

    test = sys.argv[1]
    output_filename = "tests_to_run"

    if "," in test:
        write_to_file(output_filename, test + "\n")
    else:
        with open(output_filename, "w") as f:
            for backend in BACKENDS:
                f.write(f"{test},{backend}\n")

if __name__ == "__main__":
    main()
