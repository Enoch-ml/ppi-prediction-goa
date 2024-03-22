import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import os
import time

# Create a Tkinter root widget
root = tk.Tk()
root.withdraw()

# Open a file dialog
txt_file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])

if txt_file_path:
    start_time = time.time()
    
    file_name = os.path.basename(txt_file_path).split('.')[0]
    df = pd.read_csv(txt_file_path, delimiter='\t')

    excel_file_path = file_name + '.xlsx'
    df.to_excel(excel_file_path, index=False)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f'Data stored in {excel_file_path}')
    print("Elapsed time:", elapsed_time, "seconds")
    messagebox.showinfo(f"Data stored in {excel_file_path}", f"Elapsed time: {elapsed_time} seconds")

else:
    print("No file selected.")