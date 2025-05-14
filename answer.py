
try:
    # Ask user for input filename
    input_filename = input("Enter the input filename: ")
    
    # Read the input file
    with open(input_filename, 'r') as input_file:
        content = input_file.readlines()
    
    # Modify content (e.g., add line numbers and convert to uppercase)
    modified_content = []
    for i, line in enumerate(content, 1):
        modified_content.append(f"Line {i}: {line.upper()}")
    
    # Create output filename by adding '_modified' to the original name
    output_filename = input_filename.rsplit('.', 1)[0] + '_modified.txt'
    
    # Write to new file
    with open(output_filename, 'w') as output_file:
        output_file.writelines(modified_content)
    
    print(f"File successfully processed! Modified content written to {output_filename}")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied when accessing '{input_filename}'.")
except IOError as e:
    print(f"Error: An I/O error occurred: {e}")
except Exception as e:
    print(f"Unexpected error occurred: {e}")