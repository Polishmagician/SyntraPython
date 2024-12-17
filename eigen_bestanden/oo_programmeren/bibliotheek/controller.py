from functies import *
import tkinter as tk
from tkinter import Tk, Text,ttk
from ctypes import windll

def on_button_click(inputtext, output_label):
    """Handle button clicks and retrieve user input."""
    keuze = inputtext.get('1.0', 'end').strip()  # Retrieve the latest input
    if keuze in functies_dict.keys():
        output_label.config(text="OK")  # Update output label
        print("ok")  # Print to console for debugging
        functies_dict[keuze]()
    else:
        output_label.config(text=f"Geen functie gevonden voor keuze: '{keuze}'")
        print("nok")  # Print to console for debugging
def main():
    windll.shcore.SetProcessDpiAwareness(1)
    root = tk.Tk()  # Call root class
    root.title('Demo mode')

    root.geometry('600x400+50+50')  # widthxheight±x±y

    # Text boxes
    text = Text(root, height=10)
    text.pack()
    text.insert('end', 'Menu\n')
    text.insert('end', '1) Toon alle *KEUZE*\n')
    text.insert('end', '2) Voeg data toe\n')
    text.insert('end', '3) Pas aan\n')
    text.insert('end','4) TBD\n')
    text['state'] = 'disabled'

    # Input text box
    inputtext = tk.Text(root, height=2)
    inputtext.pack()

    # Output label
    output_label = tk.Label(root, text="Voer een keuze in (1, 2, 3, etc.).", font=("Helvetica", 12))
    output_label.pack(pady=20)

    # Go button
    gobutton = ttk.Button(
        root,
        text='Go',
        command=lambda: on_button_click(inputtext, output_label)  # Pass inputtext and output_label
    )
    gobutton.pack(ipadx=5, ipady=5, expand=True)

    root.mainloop()

    """Hoofdmenu voor interactie."""
    while True:
        break
        # print("\nMenu:")
        # print("1) Toon alle *KEUZE*")
        # print("2) Voeg data toe")
        # print("3) Pas aan")
        # print("4) TBD")
        # print("5) TBD")
        # print("6) TBD")
        # print("STOP) Stoppen")
        #
        # keuze = input("Maak een keuze: ").upper()
        # if keuze == "STOP":
        #     print("Programma gestopt")
        #     break
        # functies_dict[keuze]()


main()