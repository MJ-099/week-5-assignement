def read_and_modify_file():
    try:
        # Ask user for the input file name
        input_filename = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("\nOriginal Content:\n" + content)

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Ask for the output filename or use a default
        output_filename = input("Enter the name for the output file (or press Enter to use 'output.txt'): ")
        if not output_filename.strip():
            output_filename = "output.txt"

        # Write modified content to new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"\n Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(" Error: The file does not exist.")
    except IOError:
        print(" Error: Could not read or write to the file.")
    except Exception as e:
        print(f" Unexpected error: {e}")

# Run the function
read_and_modify_file()
