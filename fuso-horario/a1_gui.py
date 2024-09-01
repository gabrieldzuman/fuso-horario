import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from time import gmtime, strftime


class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("World Clocks")

        self.time_zones = {
            "UTC": 0,
            "EST": -5,
            "CST": -6,
            "MST": -7,
            "PST": -8,
            "IST": 5.5,
            "JST": 9
        }

        self.create_widgets()

        self.update_clocks()

    def create_widgets(self):
        self.frames = {}
        self.labels = {}

        for i, tz in enumerate(self.time_zones.keys()):
            frame = ttk.Frame(self.root, padding="10")
            frame.grid(row=i, column=0)

            label = ttk.Label(frame, text=tz, font=("Helvetica", 20))
            label.grid(row=0, column=0, padx=10)

            time_label = ttk.Label(frame, text="", font=("Helvetica", 20))
            time_label.grid(row=0, column=1, padx=10)

            self.frames[tz] = frame
            self.labels[tz] = time_label

    def update_clocks(self):
        for tz, offset in self.time_zones.items():
            utc_time = datetime.utcnow()
            local_time = utc_time + timedelta(hours=offset)
            time_str = local_time.strftime("%H:%M:%S")
            self.labels[tz].config(text=time_str)

        self.root.after(1000, self.update_clocks)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
