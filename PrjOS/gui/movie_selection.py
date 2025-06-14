def show_movie_selection(root, username):
    import tkinter as tk
    from PIL import Image, ImageTk
    import os
    from gui.select_time import show_time_selection
    from gui.login_screen import show_login_screen
    from utils.file_handler import read_json
    from config.settings import MOVIES_FILE  

    ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("800x600")
    tk.Label(root, text=f"Welcome, {username}!", font=("Arial", 18)).pack(pady=10)
    tk.Label(root, text="Available Movies Today", font=("Arial", 14)).pack(pady=5)

    scroll_frame_container = tk.Frame(root)
    scroll_frame_container.pack(fill="both", expand=True, padx=10)

    canvas = tk.Canvas(scroll_frame_container)
    scrollbar = tk.Scrollbar(scroll_frame_container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    movies = read_json(MOVIES_FILE)

    for movie in movies:
        frame = tk.Frame(scrollable_frame, pady=10)
        frame.pack(fill="x", padx=20)

        img_path = os.path.join(ASSETS_DIR, movie["image"])
        try:
            img = Image.open(img_path)
            img = img.resize((150, 220))
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(frame, image=photo)
            img_label.image = photo
            img_label.pack(side="left", padx=10)
        except:
            tk.Label(frame, text="[Image Not Found]").pack(side="left", padx=10)

        info_frame = tk.Frame(frame)
        info_frame.pack(side="left", fill="x", expand=True, padx=10)

        tk.Label(info_frame, text=movie["title"], font=("Arial", 14, "bold"), anchor="w").pack(anchor="w")
        tk.Button(info_frame, text="Select Showtime", font=("Arial", 12),
                  command=lambda m=movie["title"]: show_time_selection(root, username, m)).pack(anchor="w", pady=10)

    tk.Button(root, text="Back to Login", font=("Arial", 12),
              command=lambda: show_login_screen(root)).pack(pady=15)
