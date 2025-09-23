import random
import webbrowser
import tkinter as tk

LINKS = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www.youtube.com/watch?v=_czzkqPjvS4",
    "https://youtu.be/cJz6Oqm4UoY?t=3",
    "https://youtu.be/DNOiKHgzMb0",
    "https://www.youtube.com/shorts/PnyIzZswc_M",
    "https://www.youtube.com/watch?v=bVp_J_wxrHY&pp=ygUYcGV0ZXIgZ3JpZmZpIG5zYXlzIG4gd29y",
]

SPIN_FRAMES = ["Spinning.", "Spinning..", "Spinning..."]

class GambleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gamble Links 🎰")
        self.resizable(False, False)

        # center the window-ish
        w, h = 360, 200
        self.geometry(f"{w}x{h}+{self.winfo_screenwidth()//2 - w//2}+{self.winfo_screenheight()//3 - h//2}")

        self.status = tk.StringVar(value="Press Enter or the button to gamble.")
        self.button = tk.Button(self, text="🎲  Gamble!", font=("Segoe UI", 14, "bold"),
                                command=self.start_spin, width=16)
        self.button.pack(pady=24)

        self.status_lbl = tk.Label(self, textvariable=self.status, font=("Segoe UI", 11))
        self.status_lbl.pack()

        self.bind("<Return>", lambda e: self.start_spin())

        # for animation
        self._spin_step = 0
        self._spinning = False
        self._spin_ticks = 0

    def start_spin(self):
        if self._spinning:
            return
        self._spinning = True
        self._spin_step = 0
        self._spin_ticks = 0
        self.button.config(state="disabled")
        self.animate_spin()

    def animate_spin(self):
        # simple non-blocking animation using .after()
        self.status.set(SPIN_FRAMES[self._spin_step % len(SPIN_FRAMES)])
        self._spin_step += 1
        self._spin_ticks += 1

        # spin for ~1.2s (about 12 frames @100ms)
        if self._spin_ticks < 12:
            self.after(100, self.animate_spin)
        else:
            self.finish_spin()

    def finish_spin(self):
        link = random.choice(LINKS)
        self.status.set(f"You got:\n{link}")
        # try opening in a new tab; if that fails, fallback to default open
        try:
            webbrowser.open_new_tab(link)
        except Exception:
            webbrowser.open(link)
        self.button.config(state="normal")
        self._spinning = False

if __name__ == "__main__":
    app = GambleApp()
    app.mainloop()
