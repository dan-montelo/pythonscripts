import rhino3dm
import tkinter as tk
from tkinter import filedialog

def get_all_blocks_in_rhino_file(file_path):
    # Load the Rhino file
    rhino_file = rhino3dm.File3dm.Read(file_path)
    
    # Check if the file was loaded successfully
    if not rhino_file:
        print("Failed to load the Rhino file.")
        return
    
    # Iterate through all instance definitions (blocks)
    for block in rhino_file.AllInstanceDefinitions:
        print(f"Block Name: {block.Name}")
        # You can access other properties of the block here

def main():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to select a Rhino file
    file_path = filedialog.askopenfilename(
        title="Select a Rhino file",
        filetypes=(("Rhino files", "*.3dm"), ("All files", "*.*"))
    )

    # Check if a file was selected
    if file_path:
        get_all_blocks_in_rhino_file(file_path)
    else:
        print("No file was selected.")

if __name__ == "__main__":
    main()