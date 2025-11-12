# My First GUI
# Dalila Spencer
# 2025-11-11

import tkinter as tk

class MyGUI:
    def __init__(self):
        # create main window
        self.main_window = tk.Tk()

        # create label widget
        self.label = tk.Label(self.main_window, text="Supercalafragilisticexpialidocious")

        # pack the label
        self.label.pack(padx=20, pady=20)

        # enter main loop
        self.main_window.mainloop()

# Create an instance of MyGUI
if __name__ == '__main__':
    gui = MyGUI()

