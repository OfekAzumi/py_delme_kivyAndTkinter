#3 buttons, every button color
import tkinter as tk
import random
# Function to be triggered when the button is clicked
def btn1_click():
    colors = ["blue", "red", "green","yellow","pink","purple","white","orange","gray"]
    num = random.randint(0,len(colors)-1)
    button1.config(bg=colors[num])

def btn2_click():
    colors = ["blue", "red", "green","yellow","pink","purple","white","orange","gray"]
    num = random.randint(0,len(colors)-1)
    button2.config(bg=colors[num])

def btn3_click():
    colors = ["blue", "red", "green","yellow","pink","purple","white","orange","gray"]
    num = random.randint(0,len(colors)-1)
    button3.config(bg=colors[num])

# Create the main application window
root = tk.Tk()
root.title("Colorful Button")

# Create a button widget with a blue background and white text
button1 = tk.Button(root, text="Click Me", command=btn1_click)
button2 = tk.Button(root, text="Click Me", command=btn2_click)
button3 = tk.Button(root, text="Click Me", command=btn3_click)

# Create a label widget to display text when the button is clicked
label = tk.Label(root, text="")

# Pack the button and label widgets
button1.pack()
button2.pack()
button3.pack()
label.pack()

# Start the Tkinter main event loop
root.mainloop()
