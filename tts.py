import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("File Loader and Saver")

# Function to open a file
file_path = ''

def open_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                text = file.read()
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to save a file
def save_file():
    text_to_save = text_box.get(1.0, tk.END)
    # file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")], defaultextension=".txt")
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(text_to_save)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create a button to open a file
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack()

# Create a text box for editing or displaying the loaded/saved text
text_box = tk.Text(root, wrap=tk.WORD, width=40, height=10)
text_box.pack()

# Create a button to save a file
save_button = tk.Button(root, text="Save File", command=save_file)
save_button.pack()

# Start the Tkinter main event loop
root.mainloop()
