import customtkinter as ctk
import constants
import logic


# --- 1. THE CREDITS WINDOW CLASS ---
class CreditsWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Credits")
        self.geometry("400x200")

        # Keep this window on top of the main one
        self.attributes("-topmost", True)

        self.label = ctk.CTkLabel(
            self,
            text="Special thanks to u/Effective_Durian_263 on\nsubreddit r/MuslimLounge for giving feedback\non audioplayer logic.",
            font=("Arial", 14),
            wraplength=350
        )
        self.label.pack(expand=True, padx=20, pady=20)


class QuranPlayerUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Quran Player app prototype V2")
        self.geometry("900x650")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # To track the credits window so only one opens at a time
        self.credits_window = None

        # --- SIDEBAR & SEARCH ---
        self.sidebar_frame = ctk.CTkFrame(self, width=250)
        self.sidebar_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # --- NEW CREDITS BUTTON ---
        self.credits_btn = ctk.CTkButton(
            self.sidebar_frame,
            text="📜 Credits",
            fg_color="transparent",
            border_width=1,
            command=self.open_credits
        )
        self.credits_btn.pack(fill="x", padx=10, pady=(10, 0))

        self.search_var = ctk.StringVar()
        self.search_var.trace_add("write", self.filter_surahs)
        self.search_entry = ctk.CTkEntry(self.sidebar_frame, placeholder_text="Search Surah...",
                                         textvariable=self.search_var)
        self.search_entry.pack(fill="x", padx=10, pady=10)

        # ... (Rest of your scroll_frame and buttons code here) ...
        self.scroll_frame = ctk.CTkScrollableFrame(self.sidebar_frame, label_text="Surah List")
        self.scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
        self.surah_buttons = []
        for i, name in enumerate(constants.listsurah):
            btn = ctk.CTkButton(self.scroll_frame, text=f"{i + 1}. {name}", anchor="w", fg_color="transparent",
                                command=lambda index=i + 1: self.on_surah_click(index))
            btn.pack(fill="x", padx=5, pady=2)
            self.surah_buttons.append({"btn": btn, "name": name.lower(), "index": str(i + 1)})

        # --- MAIN CONTENT ---
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.reciter_dropdown = ctk.CTkOptionMenu(self.main_frame, values=list(constants.RECITERS.keys()))
        self.reciter_dropdown.pack(pady=20)

        self.status_label = ctk.CTkLabel(self.main_frame, text="Select a Surah", font=("Arial", 18, "bold"))
        self.status_label.pack(pady=(40, 10))

        self.play_btn = ctk.CTkButton(self.main_frame, text="▶ PLAY", font=("Arial", 16, "bold"),
                                      fg_color="#2ecc71", hover_color="#27ae60", height=45,
                                      command=self.toggle_play)
        self.play_btn.pack(pady=20)

        self.seeker = ctk.CTkSlider(self.main_frame, from_=0, to=1, command=logic.seek)
        self.seeker.set(0)
        self.seeker.pack(fill="x", padx=50, pady=(20, 0))

        self.time_label = ctk.CTkLabel(self.main_frame, text="00:00 / 00:00")
        self.time_label.pack(pady=5)

        self.vol_container = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.vol_container.pack(side="bottom", pady=40)
        self.vol_label = ctk.CTkLabel(self.vol_container, text="70%", font=("Arial", 14, "bold"))
        self.vol_label.pack()
        self.volume_slider = ctk.CTkSlider(self.vol_container, from_=0, to=100, command=self.on_volume_change)
        self.volume_slider.set(70)
        self.volume_slider.pack()

        self.is_playing = False
        self.update_ui_loop()

    # --- NEW OPEN CREDITS FUNCTION ---
    def open_credits(self):
        if self.credits_window is None or not self.credits_window.winfo_exists():
            self.credits_window = CreditsWindow(self)
        else:
            self.credits_window.focus()

    def filter_surahs(self, *args):
        query = self.search_var.get().lower()
        for item in self.surah_buttons:
            if query in item["name"] or query in item["index"]:
                item["btn"].pack(fill="x", padx=5, pady=2)
            else:
                item["btn"].pack_forget()

    def on_surah_click(self, index):
        self.is_playing = False
        self.play_btn.configure(text="▶ PLAY", fg_color="#2ecc71")
        selected_reciter = self.reciter_dropdown.get()
        surah_name = constants.listsurah[index - 1]
        self.status_label.configure(text=f"Ready: {surah_name}\n({selected_reciter})")
        logic.play_request(index, selected_reciter)

    def toggle_play(self):
        if not self.is_playing:
            logic.player.play()
            self.is_playing = True
            self.play_btn.configure(text="⏸ PAUSE", fg_color="#e67e22")
        else:
            logic.player.pause()
            self.is_playing = False
            self.play_btn.configure(text="▶ PLAY", fg_color="#2ecc71")

    def on_volume_change(self, value):
        self.vol_label.configure(text=f"{int(value)}%")
        logic.set_volume(value)

    def update_ui_loop(self):
        current_ms, total_ms = logic.player.get_time_info()
        if total_ms > 0:
            self.time_label.configure(text=f"{logic.format_time(current_ms)} / {logic.format_time(total_ms)}")
            self.seeker.set(current_ms / total_ms)
        self.after(500, self.update_ui_loop)


if __name__ == "__main__":
    app = QuranPlayerUI()
    app.mainloop()