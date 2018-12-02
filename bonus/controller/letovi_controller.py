import sqlite3
from model.let import Let
from model.karta import Karta

DB_PATH = 'C:\\Users\\vidpl\PycharmProjects\\bonus\\db\\bonus.db'


def connect():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    conn.commit()
    return conn


def get_all_flights():
    conn = connect()
    c = conn.cursor()

    query = """SELECT * FROM letovi"""
    c.execute(query)

    flights_data = c.fetchall()
    flights = []

    for flight in flights_data:
        new_flight = Let(flight[0], flight[1], flight[2], flight[3], flight[4], flight[5], flight[6], flight[7], flight[8], flight[9], flight[10], flight[11])
        flights.append(new_flight)
    return flights


def flight_lookup(dep, arr):
    conn = connect()
    c = conn.cursor()
    query = """SELECT * FROM letovi WHERE origin=? AND dest=?"""

    c.execute(query, (dep, arr))
    flights_data = c.fetchall()
    flights = []

    for flight in flights_data:
        new_flight = Let(flight[0], flight[1], flight[2], flight[3], flight[4], flight[5], flight[6], flight[7],
                         flight[8], flight[9], flight[10], flight[11])
        flights.append(new_flight)

    return flights


def get_flight(broj_leta):
    conn = connect()
    c = conn.cursor()
    query = "SELECT * FROM letovi WHERE broj_leta=?"

    c.execute(query, (broj_leta,))
    flight = c.fetchone()
    new_flight = Let(flight[0], flight[1], flight[2], flight[3], flight[4], flight[5], flight[6], flight[7],
                     flight[8], flight[9], flight[10], flight[11])
    return new_flight


def reserve_ticket(broj_leta, data):
    if data['class'] != 'economy' and data['class'] != 'business' and data['class'] != 'first':
        return 400
    conn = connect()
    c = conn.cursor()
    select_query = "SELECT * FROM letovi WHERE broj_leta=?"
    c.execute(select_query, (broj_leta,))
    flight = c.fetchone()
    flight_obj = Let(flight[0], flight[1], flight[2], flight[3], flight[4], flight[5], flight[6], flight[7], flight[8], flight[9], flight[10], flight[11])


    if (data['class'] == 'economy' and flight_obj.economy_free < 1) or (data['class'] == 'business' and flight_obj.business_free < 1) or (data['class'] == 'first' and flight_obj.first_free < 1):
        return 403

    flight_obj.dec_free(data['class'])

    karta = Karta(data['fname'], data['lname'], data['class'], broj_leta, return_flight=(data['return_flight'] if data['return_flight'] is not None else 'NONE'))

    c.execute("INSERT INTO karte (uuid, fname, lname, class, flight_number, return_flight) VALUES (?, ? , ? ,? , ?, ?)", (str(karta.uuid), karta.fname, karta.lname, karta.seat_class, karta.flight_number, karta.return_flight))
    conn.commit()
    conn.close()

    return karta.to_dict()
