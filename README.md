# convert-webp
Python script to convert .webp image files to .jpeg files

This is a Python3 script that uses the Pillow library to convert all .webp files in a directory to .jpeg format, creating copies while preserving the original files. I built this in about 5 minutes use Grok with this prompt:

"I have a computer running macOS 15.5 Sequoia. On that computer I have a directory containing several image files in .webp format. I want to convert the files to .jpeg format."

How to Use:

-Install Pillow (if not already installed):
-Save the Script:
-Modify the Directory Path (if needed):

Run the Script:

What the Script Does:

-Scans the specified directory for files ending in .webp (case-insensitive).
-For each .webp file, creates a copy with the same name but a .jpeg extension.
-Converts the image to RGB format (required for JPEG) and saves it with high quality (95/100).
-Prints success or error messages for each file.
-Leaves original .webp files unchanged.

Notes:

macOS Compatibility: This script works on macOS 15.5 Sequoia, as Python and Pillow are fully compatible.

Quality: The JPEG quality is set to 95 to balance file size and image fidelity. You can adjust the quality parameter (0–100) if needed.

Error Handling: The script handles common errors (e.g., corrupt files, permission issues) and reports them without crashing.
Dependencies: Requires Python (pre-installed on macOS) and the Pillow library.

File Overwrites: If a .jpeg file with the same name already exists, it will be overwritten.

Note that the instructions from Grok say to install Pillow using pip, but instead I used Homebrew (https://brew.sh), since that's how I have Python installed. To install Pillow via Homebrew, do "brew install pillow". 
