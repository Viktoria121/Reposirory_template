import pandas as pd

def input_from_cons():
    """
    Reads text input from the console.

    Examples:
        >>> # user types 'Hello'
        >>> input_text_console()
        'Hello'

    Returns:
        str: Text entered by the user.
    """
    try:
        text = input("Enter text: ")
        return text
    except Exception as e:
        print(f"Error reading from console: {e}")
        return ""

def input_from_file_builtin():
    """
    Reads text from a file using Python's built-in functions.

    Examples:
        >>> # file 'data/input.txt' contains 'Hello World'
        >>> input_text_file_builtin()
        'Hello World'

    Returns:
        str: Contents of the file, or empty string if error occurs.
    """
    file_path = input("Enter file path: ")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def input_from_file_pandas():
    """
    Reads data from a file using pandas.

    Examples:
        >>> # file 'data/input.csv' contains CSV data
        >>> input_text_file_pandas()
           col1  col2
        0     1     2

    Returns:
        pd.DataFrame: DataFrame with file contents, or empty DataFrame if error occurs.
    """
    file_path = input("Enter CSV file path: ")
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return pd.DataFrame()