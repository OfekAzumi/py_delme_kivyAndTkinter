#notepad
#in a menu - open, save
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

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
                text_box.delete(1.0, tk.END)
                text_box.insert(1.0, 'saved to file')
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
# Create the main application window
root = tk.Tk()
root.title("NotePad")

# Create a button widget with a blue background and white text
buttons_frame = tk.Frame(root)

open_button = tk.Button(buttons_frame, text="Open File", command=open_file)
save_button = tk.Button(buttons_frame, text="Save File", command=save_file)

text_box = tk.Text(root, wrap=tk.WORD, width=40, height=10)

# Pack the buttons inside the frame horizontally
open_button.pack(side="left")
save_button.pack(side="left")

# Pack the label and button frame
buttons_frame.pack()
text_box.pack()


# Start the Tkinter main event loop
root.mainloop()