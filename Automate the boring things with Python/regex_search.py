import os
import re

def search_in_files(folder_path, regex_pattern):
    # Get a list of all .txt files in the folder
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    # Iterate through each .txt file
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)

        # Open the file and search for matching lines
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if re.search(regex_pattern, line):
                    print(f"File: {txt_file}, Line: {line_number}: {line.strip()}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    regex_pattern = input("Enter the regular expression pattern: ")

    try:
        search_in_files(folder_path, regex_pattern)
    except OSError as e:
        print(f"Error: {e}")
