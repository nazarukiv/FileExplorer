# FileExplorer
# File Search and Copy Utility

## Overview

This Python program allows users to search for files containing a specific keyword within a specified directory and its subdirectories. It then copies those files to another specified location.

## Usage

1. **Installation:**
   - Ensure you have Python installed on your system.
   - Clone or download the script to your local machine.

2. **How to Use:**
   - Run the script using Python.
   - You will be prompted to enter the keyword you want to search for and the directory from which to start the search.
   - Next, provide the directory where the matching files should be copied.
   - The program will search for files with the `.txt` extension containing the specified keyword and copy them to the specified destination directory.

3. **Error Handling:**
   - If any errors occur during the search or copy process, they will be logged in an `errors.txt` file within the destination directory.

4. **Note:**
   - This program is designed to search for `.txt` files specifically. You can modify the file extension criteria within the script if needed.

## Example

Suppose you want to search for files containing the keyword "important" within the directory `/Users/user/Documents`. You want to copy these files to `/Users/user/Backup`.

```shell
python search.py
