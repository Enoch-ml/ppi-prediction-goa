"""
============
parse_gaf.py
============

Parses a GAF file "{file_name}.gaf" into an array
Removes all comments, which are lines that begin with '!'

==========
Created by Enoch Lee for final project for BIOENGR 175.
BIOENGR 175 (Machine Learning and Data-Driven Modeling in Bioengineering) is a course at UCLA taught by Dr. Aaron Meyer

"""


import tkinter as tk
from tkinter import filedialog

def select_gaf_file():
    """
    Function to open a file dialog and select a GAF file.
    
    Returns:
    - The path of the selected GAF file, or None if no file is selected.
    """
    # Create Tkinter root window
    root = tk.Tk()
    root.withdraw()

    # Select the GAF file
    gaf_file_path = filedialog.askopenfilename(title="Select GAF file", filetypes=(("GAF files", "*.gaf"), ("All files", "*.*")))
    
    return gaf_file_path


def read_gaf_file(file_path):
    """
    Reads a GAF file, removes lines that begin with "!", and splits each line at the tab character ('\t').
    
    Args:
    - file_path: The path of the GAF file to read.
    
    Returns:
    - A list of lists, where each inner list contains the substrings of a non-comment line split at '\t'.
    """
    
    gaf_data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line.startswith('!'):
                    line_data = line.split('\t')
                    gaf_data.append(line_data)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return gaf_data


def print_first_n_lines(data, n):
    print(f"Displaying first {n} lines:")
    for row in data[:n]:
        print(row)



selected_file = select_gaf_file()

if selected_file:
    print("Selected", selected_file)
    gaf_data = read_gaf_file(selected_file)
    
    if gaf_data:
        print_first_n_lines(gaf_data, n=5)

    else:
        print("No data to display.")
        
else:
    print("No file selected.")

    
