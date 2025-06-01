def show_time_selection(root, username, movie_title):
    import tkinter as tk
    from gui.seat_booking import show_seat_booking
    from gui.movie_selection import show_movie_selection
    from utils.file_handler import read_json
    from config.settings import SHOWTIMES_FILE  

    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x600") 

    tk.Label(root, text=f"{movie_title}", font=("Arial", 18, "bold")).pack(pady=20)
    tk.Label(root, text="Select a showtime", font=("Arial", 14)).pack(pady=10)

    all_times = read_json(SHOWTIMES_FILE)
    times = all_times.get(movie_title, [])


    def select_time(time_str):
        show_seat_booking(root, username, f"{movie_title} - {time_str}")

    for t in times:
        tk.Button(root, text=t, width=20, height=2, font=("Arial", 12),
                  command=lambda x=t: select_time(x)).pack(pady=10)

    tk.Button(root, text="Back", font=("Arial", 12),
              command=lambda: show_movie_selection(root, username)).pack(pady=20)
