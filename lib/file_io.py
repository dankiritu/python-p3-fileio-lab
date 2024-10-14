def write_file(file_name, file_content):
    """Writes content to a file."""
    # Make sure to write to a file with the correct extension (.txt)
    with open(f'{file_name}.txt', 'w') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    """Appends content to a file."""
    # Make sure to append to a file with the correct extension (.txt)
    with open(f'{file_name}.txt', 'a') as file:
        file.write(append_content)


def read_file(file_name):
    """Reads content from a file and returns it."""
    # Make sure to read from a file with the correct extension (.txt)
    try:
        with open(f'{file_name}.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None
