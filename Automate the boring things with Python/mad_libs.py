import re

# Read the content of a text file
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Replace placeholders with user input
def replace_placeholders(text):
    placeholders = re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB', text)
    for placeholder in placeholders:
        replacement = input(f"Enter a {placeholder.lower()}: ")
        text = text.replace(placeholder, replacement, 1)
    return text

# Main program
def main():
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    # Read the input text file
    original_text = read_file(input_file_path)

    # Replace placeholders with user input
    mad_libs_text = replace_placeholders(original_text)

    # Write the updated text to the output file
    with open(output_file_path, 'w') as file:
        file.write(mad_libs_text)

    print("Mad Libs text has been created successfully!")

if __name__ == "__main__":
    main()
