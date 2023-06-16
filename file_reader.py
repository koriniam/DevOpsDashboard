def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("File Contents:\n", contents)
    except FileNotFoundError:
        print("File not found.")

# Usage example
file_path = input("Enter the file path: ")
read_file(file_path)
