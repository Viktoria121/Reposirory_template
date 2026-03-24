from app.io import input as io_input
from app.io import output as io_output

def main():
    console_text = io_input.input_text_console()
    
    file_text = io_input.input_text_file_builtin()
    
    pandas_data = io_input.input_text_file_pandas()
    
    io_output.output_text_console("Console input:")
    io_output.output_text_console(console_text)
    
    io_output.output_text_console("\nFile input (builtin):")
    io_output.output_text_console(file_text)
    
    io_output.output_text_console("\nFile input (pandas):")
    io_output.output_text_console(str(pandas_data))
    
    combined_text = f"Console input:\n{console_text}\n\nFile input:\n{file_text}\n\nPandas data:\n{pandas_data}"
    io_output.output_text_file_builtin(combined_text)

if __name__ == "__main__":
    main()