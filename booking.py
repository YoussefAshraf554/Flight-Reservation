import tkinter as tk
from tkinter import ttk, messagebox
from database import add_reservation

class BookingPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=16)
        self.controller = controller

        ttk.Label(self, text="Book a Flight", font=("Segoe UI", 16, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 16))

        self.name_var = tk.StringVar()
        self.flight_var = tk.StringVar()
        self.departure_var = tk.StringVar()
        self.destination_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.seat_var = tk.StringVar()

        form = ttk.Frame(self)
        form.grid(row=1, column=0, columnspan=2, sticky="nsew")

        labels = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
        vars_ = [self.name_var, self.flight_var, self.departure_var, self.destination_var, self.date_var, self.seat_var]

        for i, (label, var) in enumerate(zip(labels, vars_)):
            ttk.Label(form, text=label).grid(row=i, column=0, sticky="w", padx=(0,8), pady=6)
            entry = ttk.Entry(form, textvariable=var, width=40)
            entry.grid(row=i, column=1, sticky="ew", pady=6)

        btns = ttk.Frame(self)
        btns.grid(row=2, column=0, columnspan=2, pady=12, sticky="ew")
        ttk.Button(btns, text="Save Reservation", command=self._save).pack(side="left", padx=(0, 8))
        ttk.Button(btns, text="Back", command=lambda: self.controller.show_frame("HomePage")).pack(side="left")

        self.columnconfigure(0, weight=1)
        form.columnconfigure(1, weight=1)

    def _save(self):
        fields = [
            self.name_var.get().strip(),
            self.flight_var.get().strip(),
            self.departure_var.get().strip(),
            self.destination_var.get().strip(),
            self.date_var.get().strip(),
            self.seat_var.get().strip(),
        ]
        if any(not f for f in fields):
            messagebox.showerror("Validation", "Please fill in all fields.")
            return

        add_reservation(*fields)
        messagebox.showinfo("Success", "Reservation saved successfully!")

        # Clear fields
        for var in (self.name_var, self.flight_var, self.departure_var, self.destination_var, self.date_var, self.seat_var):
            var.set("")
