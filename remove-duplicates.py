import os
import re

# Set your folder path here
folder_path = "/path/to/your/folder"

# Regex pattern to match filenames like 'image(1).jpg'
duplicate_pattern = re.compile(r"^(.*)\(\d+\)(\.\w+)$")

for filename in os.listdir(folder_path):
    match = duplicate_pattern.match(filename)
    if match:
        original_name = match.group(1) + match.group(2)
        original_path = os.path.join(folder_path, original_name)
        duplicate_path = os.path.join(folder_path, filename)

        if os.path.exists(original_path):
            print(f"Removing duplicate: {filename}")
            os.remove(duplicate_path)
