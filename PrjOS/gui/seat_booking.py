def show_seat_booking(root, username, movie_title):
    import tkinter as tk
    from utils.file_handler import read_json
    from config.settings import SEATS_FILE
    from gui.payment_screen import show_payment_screen
    from gui.select_time import show_time_selection

    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("800x600")

    booking_key = f"{movie_title}"
    seat_data = read_json(SEATS_FILE)
    booked_seats = seat_data.get(booking_key, {})

    selected_seats = set()  

    main_frame = tk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(main_frame, text=f"{username}, select your seat for:", font=("Arial", 14)).pack()
    tk.Label(main_frame, text=movie_title, font=("Arial", 14, "bold")).pack(pady=(0, 10))

    seat_frame = tk.Frame(main_frame)
    seat_frame.pack()

    buttons = {} 

    def toggle_seat(seat_id):
        if seat_id in selected_seats:
            selected_seats.remove(seat_id)
            buttons[seat_id].config(bg="SystemButtonFace")  
        else:
            selected_seats.add(seat_id)
            buttons[seat_id].config(bg="lightgreen")

    for i in range(5):
        for j in range(5):
            seat_id = f"{chr(65 + i)}{j + 1}"
            btn = tk.Button(seat_frame, text=seat_id, width=4)
            btn.grid(row=i, column=j, padx=5, pady=5)

            if seat_id in booked_seats:
                btn.config(bg="gray", state="disabled")
            else:
                btn.config(command=lambda s=seat_id: toggle_seat(s))
                buttons[seat_id] = btn

    def proceed_to_payment():
        if selected_seats:
            show_payment_screen(root, username, movie_title, list(selected_seats))
        else:
            tk.messagebox.showwarning("No Seats", "Please select at least one seat.")

    tk.Button(main_frame, text="Proceed to Payment", font=("Arial", 12),
              command=proceed_to_payment).pack(pady=10)

    tk.Button(main_frame, text="Back", font=("Arial", 12),
              command=lambda: show_time_selection(root, username, movie_title.split(" - ")[0])
              ).pack(pady=10)
