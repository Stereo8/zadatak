import uuid


class Karta:
    def __init__(self, fname, lname, seat_class, flight_number, return_flight=None, uuid=uuid.uuid4()):
        self.fname = fname
        self.lname = lname
        self.seat_class = seat_class
        self.flight_number = flight_number
        self.return_flight = return_flight
        self.uuid = uuid

    def to_dict(self):
        json = {
            'uuid': self.uuid,
            'fname': self.fname,
            'lname': self.lname,
            'class': self.seat_class,
            'flight_number': self.flight_number,
            'return_flight': self.return_flight
        }
        return json
