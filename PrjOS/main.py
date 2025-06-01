import tkinter as tk
from gui.login_screen import show_login_screen

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")  # scale window
    root.title("Online Ticket Selling System")
    show_login_screen(root)
    root.mainloop()
    
