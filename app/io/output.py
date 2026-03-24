def output_in_cons(text):
    """
    Prints text to the console.

    Examples:
        >>> output_text_console("Hello")
        Hello

    Args:
        text (str): Text to print.
    """
    try:
        print(text)
    except Exception as e:
        print(f"Error printing to console: {e}")

def output_in_file_builtin(text):
    """
    Writes text to a file using Python's built-in functions.

    Examples:
        >>> output_text_file_builtin("Hello World")
        # Writes text to the file specified by user input

    Args:
        text (str): Text to write to file.
    """
    file_path = input("Enter file path to save: ")
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(f"Error writing to file: {e}")