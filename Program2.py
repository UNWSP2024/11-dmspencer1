# Show Info GUI
# Dalila Spencer
# 2025-11-11
import tkinter
import tkinter as tk
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # create main window
        self.main_window = tk.Tk()

        # creates button that executes display_info
        self.my_button = tk.Button(self.main_window, text="Show Info", command=self.display_info)

        # creates a quit button
        self.quit_button = tk.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        # pack the button
        self.my_button.pack(padx=20, pady=20)
        self.quit_button.pack(padx=20, pady=20)

        # enter main loop
        tk.mainloop()

        # function for my_button
    def display_info(self):
        # displays info dialogue box
        tk.messagebox.showinfo("Info", '''Dalila Spencer
         123 Main Street
        Anytown, MN 12345''')

# create an instance of MyGui
if __name__ == "__main__":
    myGUI = MyGUI()
