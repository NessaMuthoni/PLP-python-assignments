def modify_content(content):
    """Modify content by converting to uppercase (example modification)."""
    return content.upper()

def process_file():
    """Ask user for a filename, read it, modify content, and write to a new file."""
    try:
        # Get filename from user
        filename = input("Enter the filename to read: ")

        # Read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify content
        modified_content = modify_content(content)

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File successfully modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read the file. Please check file permissions.")

# Run the file processing function
process_file()
