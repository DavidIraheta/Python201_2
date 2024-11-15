# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.
from pathlib import Path
import csv
# Dictionary to count file types
file_count = {}

# Define paths
desktop = Path.home() / "Desktop"
screenshot_folder = desktop / "untitled folder"
screenshot_folder.mkdir(exist_ok=True)  # Create Screenshots folder if it doesn't exist

# Loop through each file on the desktop
for file in desktop.iterdir():
    if file.is_file():  # Only process files, not directoriesa
        file_extension = file.suffix.lower()
        
        # Update file count dictionary
        file_count[file_extension] = file_count.get(file_extension, 0) + 1
        
        # Move screenshots to the screenshot folder
        if "screenshot" in file.stem.lower():
            destination = screenshot_folder / file.name
            if destination.exists():  # Handle duplicate files by renaming
                destination = screenshot_folder / f"copy_of_{file.name}"
            file.rename(destination)

csv_path = desktop / "file_count.csv"

with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Extension", "Count"])
    for ext, count in file_count.items():
        writer.writerow([ext, count])
        
for ext, count in file_count.items():
    print(f"There are {count} file(s) with the '{ext}' extension on your desktop.")

# Print the count of each file type
# for ext, count in file_count.items():
#     print(f"There are {count} file(s) with the '{ext}' extension on your desktop.")
