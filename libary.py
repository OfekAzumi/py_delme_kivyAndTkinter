# display image,
#2 button displays different images

import tkinter as tk
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("Image Display")

# Load the image using PIL
image = Image.open("path_to_your_image.jpg")  # Replace with the path to your image file

# Convert the PIL image to a Tkinter-compatible format
tk_image = ImageTk.PhotoImage(image)

# Create a label widget to display the image
image_label = tk.Label(root, image=tk_image)

# Pack the label widget to display the image
image_label.pack()

# Start the Tkinter main event loop
root.mainloop()
