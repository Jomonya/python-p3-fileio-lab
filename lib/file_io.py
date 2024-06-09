def write_file(file_name, file_content):
    pass
    full_file_name = f"{file_name}.txt"
    # Open the file in write mode, which will create or overwrite the file
    with open(full_file_name, 'w') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    pass
    full_file_name = f"{file_name}.txt"
    # Open the file in append mode, which will create the file if it doesn't exist
    with open(full_file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    pass
    full_file_name = f"{file_name}.txt"
    # Open the file in read mode and return its content
    with open(full_file_name, 'r') as file:
        return file.read()
