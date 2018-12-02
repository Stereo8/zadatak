class Let:
    def __init__(self, broj_leta, origin, destination, dep_time, arr_time, economy, business, first, economy_free, business_free, first_free, status=None):
        self.broj_leta = broj_leta
        self.origin = origin
        self.destination = destination
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.economy = economy
        self.business = business
        self.first = first
        self.economy_free = economy_free
        self.business_free = business_free
        self.first_free = first_free
        self.status = status

    def dec_free(self, seat_class):
        if seat_class == 'economy':
            self.economy_free = self.economy_free - 1
            return self.economy_free
        if seat_class == 'business':
            self.business_free = self.business_free - 1
            return self.economy_free
        if seat_class == 'first':
            self.first_free = self.first_free - 1
            return self.economy_free
        else:
            raise ValueError

    def to_dict(self):
        json = {
            'broj_leta': self.broj_leta,
            'origin': self.origin,
            'destination': self.destination,
            'dep_time': self.dep_time,
            'economy': self.economy,
            'business': self.business,
            'first': self.first,
            'economy_free': self.economy_free,
            'business_free': self.business_free,
            'first_free': self.first_free,
            'status': self.status,
        }
        return json
