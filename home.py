import tkinter as tk
from tkinter import ttk

class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=24)
        self.controller = controller

        title = ttk.Label(self, text="Flight Reservation System", font=("Segoe UI", 20, "bold"))
        #subtitle = ttk.Label(self, text="Tkinter + SQLite", font=("Segoe UI", 11))

        btn_book = ttk.Button(self, text="Book Flight", command=lambda: controller.show_frame("BookingPage"))
        btn_view = ttk.Button(self, text="View Reservations", command=lambda: controller.show_frame("ReservationsPage"))

        title.grid(row=0, column=0, sticky="w", pady=(0, 8))
        #subtitle.grid(row=1, column=0, sticky="w", pady=(0, 24))
        btn_book.grid(row=2, column=0, sticky="ew", pady=6)
        btn_view.grid(row=3, column=0, sticky="ew", pady=6)

        self.columnconfigure(0, weight=1)
