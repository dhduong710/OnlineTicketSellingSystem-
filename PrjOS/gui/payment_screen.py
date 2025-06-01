def show_payment_screen(root, username, movie_title, seat_ids):
    import tkinter as tk
    from tkinter import messagebox
    from gui.movie_selection import show_movie_selection
    from config.settings import SEATS_FILE
    from utils.file_handler import read_json, write_json
    from gui.seat_booking import show_seat_booking

    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x600")

    def confirm_payment():
        seat_data = read_json(SEATS_FILE)
        if movie_title not in seat_data:
            seat_data[movie_title] = {}

        for seat_id in seat_ids:
            seat_data[movie_title][seat_id] = username

        write_json(SEATS_FILE, seat_data)

        messagebox.showinfo("Payment", f"Payment successful for seats: {', '.join(seat_ids)}")
        show_seat_booking(root, username, movie_title)

    def cancel_payment():
        show_seat_booking(root, username, movie_title)

    tk.Label(root, text=f"User: {username}", font=("Arial", 14)).pack(pady=10)
    tk.Label(root, text=f"Movie: {movie_title}", font=("Arial", 14)).pack(pady=10)
    tk.Label(root, text=f"Seats: {', '.join(seat_ids)}", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="Pay Now", font=("Arial", 12), command=confirm_payment).pack(pady=15)
    tk.Button(root, text="Back", font=("Arial", 12), command=cancel_payment).pack(pady=5)
