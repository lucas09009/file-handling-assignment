def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print("\nFile content:\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

if __name__ == "__main__":
    main()
