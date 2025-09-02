import tkinter as tk
from tkinter import ttk, messagebox
from database import get_all_reservations, delete_reservation

class ReservationsPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, padding=12)
        self.controller = controller

        header = ttk.Frame(self)
        header.grid(row=0, column=0, sticky="ew", pady=(0,10))
        ttk.Label(header, text="Reservations", font=("Segoe UI", 16, "bold")).pack(side="left")
        ttk.Button(header, text="Refresh", command=self.refresh).pack(side="right", padx=(6,0))
        ttk.Button(header, text="Back", command=lambda: controller.show_frame("HomePage")).pack(side="right", padx=(6,0))

        columns = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=12)
        for col in columns:
            self.tree.heading(col, text=col.replace("_"," ").title())
            self.tree.column(col, width=120 if col!="name" else 180, anchor="center")
        self.tree.grid(row=1, column=0, sticky="nsew")

        actions = ttk.Frame(self)
        actions.grid(row=2, column=0, sticky="ew", pady=10)
        ttk.Button(actions, text="Edit Selected", command=self._edit_selected).pack(side="left")
        ttk.Button(actions, text="Delete Selected", command=self._delete_selected).pack(side="left", padx=8)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # Initial load
        self.refresh()

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for r in get_all_reservations():
            self.tree.insert("", "end", values=(r["id"], r["name"], r["flight_number"],
                                                r["departure"], r["destination"], r["date"], r["seat_number"]))

    def _selected_id(self):
        sel = self.tree.selection()
        if not sel:
            return None
        values = self.tree.item(sel[0], "values")
        return int(values[0]) if values else None

    def _edit_selected(self):
        res_id = self._selected_id()
        if res_id is None:
            messagebox.showwarning("Edit", "Please select a reservation to edit.")
            return
        self.controller.show_frame("EditReservationPage", res_id=res_id)

    def _delete_selected(self):
        res_id = self._selected_id()
        if res_id is None:
            messagebox.showwarning("Delete", "Please select a reservation to delete.")
            return
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?"):
            delete_reservation(res_id)
            self.refresh()
