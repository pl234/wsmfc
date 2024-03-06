import json
from pathlib import Path

import withoutStoring_mand_nested as mn
import withoutStoring_mand_text_updated as mt

import tkinter as tk
from tkinter import filedialog

def process_folder(folder_path):
    total_data = {}
    file_processing_functions = {
        '.txt': mt.func3,
        '.json': mn.func2
    }
    for file_path in Path(folder_path).glob('**/*'):
        file_name=file_path.name
        if file_path.is_file() and file_name not in["Test_ALL_results.json","FORMAT.json"]:
            file_type = file_path.suffix.lower()
            if file_type in file_processing_functions:
                process_func = file_processing_functions[file_type]
                data = process_func(format_file_path, file_path)
                total_data[file_path.name] = data
    return total_data

def select_folder_Format():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory(title="Select a Folder to process the files")
    format_file_path=filedialog.askopenfilename(title="Select the FORMAT file")
    return folder_path,format_file_path

# format_file_path = r"FORMAT.json"
# folder_path = r"C:\Users\101798\OneDrive - UNIPHORE SOFTWARE SYSTEMS PVT LTD\withoutStoring_mand_folder"

folder_path,format_file_path=select_folder_Format()
total_data = process_folder(folder_path)

final_output_path = "Test_ALL_results.json"
try:
    with open(final_output_path, 'w') as final:
        json.dump(total_data, final, indent=4)
        print(f"Results are available in '{final_output_path}'")
except Exception as e:
    print(f"An error occurred: {e}")

