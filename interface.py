import tkinter as tk

# Function to update the label with the entered text
def update_label():
    text = entry.get()
    label.config(text=f"You typed: {text}")

# Create the main application window
root = tk.Tk()
root.title("Basic Tkinter Example")
root.geometry("700x500")  # Set window size

# Create a label
label = tk.Label(root, text="Enter something below:", font=("Arial", 12))
label.pack(pady=10)

# Create an entry field
entry = tk.Entry(root, width=25)
entry.pack()

# Create a button
button = tk.Button(root, text="Submit", command=update_label)
button.pack(pady=10)

# Start the main event loop
root.mainloop()
