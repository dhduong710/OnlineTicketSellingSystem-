def show_login_screen(root):
    import tkinter as tk
    from tkinter import messagebox
    from gui.movie_selection import show_movie_selection
    from core.user_manager import authenticate_user, register_user
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x600")  

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if authenticate_user(username, password):
            messagebox.showinfo("Login Success", "Welcome!")
            show_movie_selection(root, username)
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def open_register_window():
        register_window = tk.Toplevel(root)
        register_window.title("Register")
        register_window.geometry("300x200")

        tk.Label(register_window, text="New Username").pack(pady=5)
        new_username_entry = tk.Entry(register_window)
        new_username_entry.pack(pady=5)

        tk.Label(register_window, text="New Password").pack(pady=5)
        new_password_entry = tk.Entry(register_window, show="*")
        new_password_entry.pack(pady=5)

        def register():
            new_username = new_username_entry.get()
            new_password = new_password_entry.get()
            if register_user(new_username, new_password):
                messagebox.showinfo("Success", "Registration successful!")
                register_window.destroy()
            else:
                messagebox.showerror("Error", "Username already exists")

        tk.Button(register_window, text="Register", command=register).pack(pady=10)

    tk.Label(root, text="Username").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)

    tk.Label(root, text="Password").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    tk.Button(root, text="Login", command=login).pack(pady=10)
    tk.Button(root, text="Register", command=open_register_window).pack()
