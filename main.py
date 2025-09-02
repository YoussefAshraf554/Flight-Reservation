import tkinter as tk
from tkinter import ttk
import sys

from database import init_db
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.geometry("900x600")
        self.minsize(800, 520)

        # Theme
        try:
            self.style = ttk.Style(self)
            if 'clam' in self.style.theme_names():
                self.style.theme_use('clam')
        except Exception:
            pass

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F, name in [(HomePage, "HomePage"),
                        (BookingPage, "BookingPage"),
                      (ReservationsPage, "ReservationsPage"),
                      (EditReservationPage, "EditReservationPage")]:
            frame = F(container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, name: str, **kwargs):
        frame = self.frames[name]
        if name == "EditReservationPage" and "res_id" in kwargs:
            frame.load_reservation(kwargs["res_id"])
        frame.tkraise()

if __name__ == "__main__":
    init_db()
    app = App()
    app.mainloop()
    
