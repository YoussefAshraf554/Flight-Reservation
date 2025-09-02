import sqlite3
from pathlib import Path

DB_NAME = "flights.db"

def _db_path():
    return str(Path(__file__).resolve().parent / DB_NAME)

def get_connection():
    conn = sqlite3.connect(_db_path())
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                flight_number TEXT NOT NULL,
                departure TEXT NOT NULL,
                destination TEXT NOT NULL,
                date TEXT NOT NULL,
                seat_number TEXT NOT NULL
            );
        """)
        conn.commit()

def add_reservation(name, flight_number, departure, destination, date, seat_number):
    with get_connection() as conn:
        cur = conn.execute("""
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (name, flight_number, departure, destination, date, seat_number))
        conn.commit()
        return cur.lastrowid

def get_all_reservations():
    with get_connection() as conn:
        cur = conn.execute("SELECT * FROM reservations ORDER BY id DESC;")
        return [dict(row) for row in cur.fetchall()]

def get_reservation(res_id: int):
    with get_connection() as conn:
        cur = conn.execute("SELECT * FROM reservations WHERE id = ?;", (res_id,))
        row = cur.fetchone()
        return dict(row) if row else None

def update_reservation(res_id: int, name, flight_number, departure, destination, date, seat_number):
    with get_connection() as conn:
        conn.execute("""
            UPDATE reservations
            SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
            WHERE id=?;
        """, (name, flight_number, departure, destination, date, seat_number, res_id))
        conn.commit()

def delete_reservation(res_id: int):
    with get_connection() as conn:
        conn.execute("DELETE FROM reservations WHERE id=?;", (res_id,))
        conn.commit()
