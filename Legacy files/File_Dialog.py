import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Hide the root window

file_path = filedialog.askopenfilename()
print(file_path)