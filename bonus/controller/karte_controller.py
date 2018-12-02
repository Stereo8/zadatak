import sqlite3
from model.karta import Karta

DB_PATH = 'C:\\Users\\vidpl\PycharmProjects\\bonus\\db\\bonus.db'


def connect():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    conn.commit()
    return conn


def get_ticket(uuid):
    conn = connect()
    c = conn.cursor()

    c.execute("SELECT * FROM karte WHERE uuid=?", (uuid,))
    ticket_row = c.fetchone()

    ticket = Karta(ticket_row[1], ticket_row[2], ticket_row[3], ticket_row[4], return_flight=ticket_row[5], uuid=uuid)

    return ticket.to_dict()


def update_ticket(uuid, data):
    conn = connect()
    c = conn.cursor()

    c.execute("UPDATE karte SET fname=?, lname=? WHERE uuid=?", (data['fname'], data['lname'], uuid))
    conn.commit()
    c.execute("SELECT * FROM karte WHERE uuid=?", (uuid,))
    ticket_row = c.fetchone()

    ticket = Karta(ticket_row[1], ticket_row[2], ticket_row[3], ticket_row[4], return_flight=ticket_row[5], uuid=uuid)

    conn.commit()
    conn.close()
    return ticket.to_dict()
