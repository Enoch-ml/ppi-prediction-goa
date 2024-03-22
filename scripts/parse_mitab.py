"""
==============
parse_mitab.py
==============

Parses a MITAB file "{file_name}.mitab" into an array with selected columns

==========
Created by Enoch Lee for final project for BIOENGR 175.
BIOENGR 175 (Machine Learning and Data-Driven Modeling in Bioengineering) is a course at UCLA taught by Dr. Aaron Meyer

"""

selected_columns = ["Alt IDs Interactor A", "Alt IDs Interactor B", "Confidence Value"]


import tkinter as tk
from tkinter import filedialog
import numpy as np

def select_mitab_file():
    """
    Function to open a file dialog and select a MITAB file.
    
    Returns:
    - The path of the selected MITAB file, or None if no file is selected.
    """
    # Create Tkinter root window
    root = tk.Tk()
    root.withdraw()

    # Select the MITAB file
    mitab_file_path = filedialog.askopenfilename(title="Select MITAB file", filetypes=(("MITAB files", "*.txt"), ("All files", "*.*")))
    
    return mitab_file_path


def read_mitab_file(file_path, selected_columns):
    """
    Reads a MITAB file and extracts specific columns.
    
    Args:
    - file_path: The path of the MITAB file to read.
    
    Returns:
    - A list of tuples, where each tuple contains the values of the desired columns.
    """
    
    extracted_data = []
    
    try:
        with open(file_path, 'r') as file:
            # Read the first line to get column names
            columns = file.readline().strip().split('\t')
            
            # Check if all selected columns are present
            missing_columns = [col for col in selected_columns if col not in columns]
            if missing_columns:
                error_message = f"Error: Selected columns not found: {', '.join(missing_columns)}"
            else:
                column_indices = [columns.index(col) for col in selected_columns]
                
                # Read the rest of the file
                for line in file:
                    values = line.strip().split('\t')
                    extracted_values = [values[i] for i in column_indices]
                    extracted_data.append(tuple(extracted_values))
                
    except FileNotFoundError:
        error_message = f"Error: File '{file_path}' not found."
        
    return extracted_data


def standardize_names(data):
    """
    Removes all instances of 'uniprotkb:' and '_HUMAN' in order to get standard UNIPROTKB names without tags
    
    """
    
    ppis = np.array([[entry.replace('uniprotkb:', '').replace('_HUMAN', '') if isinstance(entry, str) else entry for entry in row] for row in data])
    return ppis


def print_first_n_lines(data, n):
    print(f"Displaying first {n} lines:")
    for row in data[:n]:
        print(row)


selected_file = select_mitab_file()
if selected_file:
    print("Selected", selected_file)
    
    mitab_data = read_mitab_file(selected_file, selected_columns)
    
    if mitab_data:
        ppis = standardize_names(mitab_data)
        
        print_first_n_lines(ppis, n=5)
        
    else:
        print("No data to display.")
    
else:
    print("No file selected.")