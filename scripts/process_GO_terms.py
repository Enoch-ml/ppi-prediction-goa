"""
===================
process_GO_terms.py
===================

Processes "go-basic.txt" into separate GO terms with their relevant attributes
Assumes "go-basic.txt" is in the directory "..\assets\go-basic.txt"
Removes attributes based on their relevance to prediction of protein-protein interactions


==========
Created by Enoch Lee for final project for BIOENGR 175.
BIOENGR 175 (Machine Learning and Data-Driven Modeling in Bioengineering) is a course at UCLA taught by Dr. Aaron Meyer

"""


import numpy as np

input_file_path = r"..\assets\go-basic.txt"
cols_to_delete = [] #[0, 2, 3, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16]


def parse_terms_from_file(file_path):
    """
    Parses input GO text file and extracts term information
    
    Returns
    1) List of terms, where each term is a dictionary with attributes (keys) that map to values
    2) Total list of attributes (keys)
    
    """
    
    attributes = set()
    terms = []
    
    
    try:
        with open(file_path, 'r') as file:
            curr_term = {}
            
            for line in file:
                line = line.strip()

                if line.startswith('[Term]'):
                    if curr_term:  # If term is not empty
                        terms.append(curr_term.copy())
                        curr_term = {}

                elif line:  # If line is not empty
                    try:
                        key, value = line.split(': ', 1)
                        value = value.split('!', 1)[0].strip() # Remove comments
                        
                        if key not in attributes:
                            attributes.add(key)
                        
                        curr_term[key] = value
                    
                    except ValueError:
                        pass

            if curr_term:
                terms.append(curr_term)
                
        return terms, list(attributes)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return [], []

    
def process_and_delete():
    # Read terms from input text file
    terms, raw_cols = parse_terms_from_file(input_file_path)
    keys = list(set().union(*(term.keys() for term in terms)))

    # Initialize array with GO term information
    raw_go_terms = np.empty((len(terms), len(keys)), dtype=object)
    for i, term in enumerate(terms):
        for j, key in enumerate(keys):
            raw_go_terms[i, j] = term.get(key, None)
    
    go_terms = np.delete(raw_go_terms, cols_to_delete, axis=1)
    cols = np.delete(raw_cols, cols_to_delete)

    return go_terms, cols


def print_first_n_lines(cols, data, n):
    print(f"Displaying first {n} lines:")
    for i in range(0, n):
        for item1, item2 in zip(cols, data[i]):
            print("{:<{width}} {}".format(item1, item2, width=15))
        print("\n")
        

go_terms, cols = process_and_delete()

if len(go_terms) != 0:
    print_first_n_lines(cols, go_terms, n=5)
else:
    print("No data to display.")