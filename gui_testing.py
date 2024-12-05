import tkinter as tk
from tkinter import Tk

def main():
    # Create the GUI
    gui = Tk()
    
    # Atur warna background GUI
    gui.configure(background="light green")
    
    # Atur judul
    gui.title("Integral Calculator")
    
    # Atur ukuran window GUI nya
    gui.geometry("400x500")
    
    # Label
    label = tk.Label(gui, text="Hello tkinter")
    label.pack() 
    
    # Button
    btn = tk.Button(gui, text="button 1")
    btn.pack()
    
    # Start GUI event loop
    gui.mainloop()

if __name__ == "__main__":
    main()