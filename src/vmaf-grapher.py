from sys import argv

from vmaf.vmaf_report import VMAFReport

def print_usage():
    # The usage pattern commonly includes the program name, which can be accessed using sys.argv[0]
    print(f"Usage: {argv[0]} <file_path>")

def main(argc: int, argv: list):

    # sys.argv contains all command-line arguments including the program name
    # sys.argv[0] is the program name, sys.argv[1] would be the first argument
    argc = len(argv)  # Get the number of arguments, including the program name
    
    if argc == 1:
        print("Missing file path.")
        print_usage()
    elif argc == 2:
        file_path = argv[1]  # Get the file path from command line
        # Now you can use file_path to do whatever you need, like loading a file or processing
        print(f"Processing file: {file_path}")
        # Assuming FromFile is a method that processes the file
        try:
            report = VMAFReport.from_file(file_path)
            print(f"Report generated successfully: {report}")
            report.show_graph()
        except Exception as e:
            print(f"Error processing file: {e}")
    elif argc > 2:
        print("Too many arguments.")
        print_usage()

if __name__ == "__main__":
    main(len(argv), argv)
