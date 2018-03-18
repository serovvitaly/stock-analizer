

class ticket:

    def __init__(self, open, high, low, close):
        self.open = float(open)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)


class momo:

    def __init__(self, mixture):
        self.mixture = mixture

    def lala(self, first_ticket, tickets):
        for ticker, ticket in tickets.items():
            delta_open  = ticket.open  - first_ticket.open
            delta_high  = ticket.high  - first_ticket.high
            delta_low   = ticket.low   - first_ticket.low
            delta_close = ticket.close - first_ticket.close
