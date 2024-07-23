import re

def clean_file(input_file, output_file):
    # Read the content of the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Define regex patterns to match unwanted text
    patterns = [
        r'^ORIGIN',       # Matches the line containing 'ORIGIN'
        r'\d+',           # Matches numbers
        r'//',            # Matches the slashes
        r'\s+',           # Matches spaces and line breaks
    ]

    # Remove unwanted patterns using regex
    cleaned_content = content
    for pattern in patterns:
        cleaned_content = re.sub(pattern, '', cleaned_content)

    # Strip any remaining whitespace from the ends
    cleaned_content = cleaned_content.strip()

    # Confirm that the cleaned content has exactly 110 characters
    if len(cleaned_content) != 110:
        raise ValueError(f"Cleaned content does not have 110 characters. It has {len(cleaned_content)} characters.")

    # Write the cleaned content to the output file
    with open(output_file, 'w') as file:
        file.write(cleaned_content)

    print("File cleaned successfully.")

# Usage
input_file = 'preproinsulin-seq.txt'
output_file = 'cleaned_preproinsulin-seq.txt'
clean_file(input_file, output_file)
