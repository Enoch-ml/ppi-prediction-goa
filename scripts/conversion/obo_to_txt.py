"""
=============
obo_to_txt.py
=============

Converts an obo file "{file_name}.obo" to a text file "{file_name}.txt"
Removes all text before first occurrence of "[Term]"
Stores result text file in directory "..\assets"


==========
Created by Enoch Lee for final project for BIOENGR 175.
BIOENGR 175 (Machine Learning and Data-Driven Modeling in Bioengineering) is a course at UCLA taught by Dr. Aaron Meyer

"""


import tkinter as tk
from tkinter import filedialog
import os


def convert_obo_to_txt(input_file_path, output_file_path):
    try:
        # Open the input OBO file for reading
        with open(input_file_path, 'r') as obo_file:
            found_term = False  # Flag to track if [Term] is found
            with open(output_file_path, 'w') as txt_file:
                # Start writing when [Term] is found
                for line in obo_file:
                    if found_term:
                        txt_file.write(line)
                    elif line.strip() == "[Term]":
                        txt_file.write(line)
                        found_term = True
        
        print(f"Conversion completed. Output saved to {output_file_path}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")

        
# Create Tkinter root window
root = tk.Tk()
root.withdraw()


# Input directory
obo_file_path = filedialog.askopenfilename(title="Select .obo file", filetypes=(("OBO files", "*.obo"), ("All files", "*.*")))

if not obo_file_path:
    print("No file selected. Exiting.")
    exit()
    
obo_file_name = os.path.splitext(os.path.basename(obo_file_path))[0]


# Output directory
output_folder = os.path.abspath(os.path.join(os.path.dirname(obo_file_path), "..", "assets"))
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
txt_file_path = os.path.join(output_folder, f"{obo_file_name}.txt")


# Convert and remove all text before "[Term]"
convert_obo_to_txt(obo_file_path, txt_file_path)