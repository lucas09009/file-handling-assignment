def main():
    input_file = "input.txt"
    output_file = "output.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
        
      
        modified_content = content.upper()

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(modified_content)

        print(f"Modified content written to {output_file} successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to file.")

if __name__ == "__main__":
    main()