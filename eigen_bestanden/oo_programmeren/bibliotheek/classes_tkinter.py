import tkinter as tk
from tkinter import simpledialog

class TkinterConsole:
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(root, wrap="word", state="disabled", height=15, width=60)
        self.text_area.pack(padx=10, pady=10)
        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<KP_Enter>", self.on_input_enter)  # Handle Enter key

        self.input_value = None  # Store user input
        self.waiting_for_input = False

    def custom_print(self, *args):
        """Mimics the print function and writes to the Tkinter text area."""
        message = " ".join(map(str, args))  # Convert all arguments to string
        self.text_area.config(state="normal")  # Make text area writable
        self.text_area.insert("end", message + "\n")  # Add the message
        self.text_area.see("end")  # Scroll to the bottom
        self.text_area.config(state="disabled")  # Make text area read-only

    def custom_input(self, prompt=""):
        """Mimics the input function and gets user input via Tkinter."""
        self.custom_print(prompt)  # Show the prompt in the text area
        self.waiting_for_input = True
        self.input_entry.focus_set()  # Focus on the input field
        self.root.wait_variable(tk.StringVar())  # Wait until Enter key is pressed
        return self.input_value  # Return the input value

    def on_input_enter(self, event):
        """Handle Enter key press to capture user input."""
        if self.waiting_for_input:
            self.input_value = self.input_entry.get().strip().upper()
            self.custom_print(self.input_value)  # Display the input in the text area
            self.input_entry.delete(0, "end")  # Clear the input field
            self.waiting_for_input = False
            self.root.quit()  # Exit the wait_variable event loop