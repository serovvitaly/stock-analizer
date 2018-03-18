

class ticket:

    def __init__(self, open, high, low, close):
        self.open = float(open)
        self.high = float(high)
        self.low = float(low)
        self.close = float(close)


class momo:

    def __init__(self, mixture):
        self.mixture = mixture

    def calc_delta(self, base_ticket, ticket):
        d_open  = 100 - ticket.open  * 100 / base_ticket.open
        d_high  = 100 - ticket.high  * 100 / base_ticket.high
        d_low   = 100 - ticket.low   * 100 / base_ticket.low
        d_close = 100 - ticket.close * 100 / base_ticket.close
        return (
            round(d_open, 2),
            round(d_high, 2),
            round(d_low, 2),
            round(d_close, 2),
        )

    def get_absolute_delta(self, tickets_sets):
        key, first_tickets_set = tickets_sets.popitem()
        output = {key: (0,0,0,0)}
        for day, tickets_set in tickets_sets.items():
            d_open = 0
            d_high = 0 
            d_low  = 0
            d_close = 0         
            for ticker, ticket in tickets_set.items():
                first_ticket = first_tickets_set[ticker]
                delta = self.calc_delta(first_ticket, ticket)
                d_open  += delta[0] * self.mixture[ticker] / 100
                d_high  += delta[1] * self.mixture[ticker] / 100
                d_low   += delta[2] * self.mixture[ticker] / 100
                d_close += delta[3] * self.mixture[ticker] / 100
            output[day] = (
                round(d_open, 2),
                round(d_high, 2),
                round(d_low, 2),
                round(d_close, 2),
            )
        return output

    def get_relative_delta(self, tickets_sets):
        key, base_tickets_set = tickets_sets.popitem()
        output = {key: (0,0,0,0)}
        for day, tickets_set in tickets_sets.items():
            d_open = 0
            d_high = 0 
            d_low  = 0
            d_close = 0         
            for ticker, ticket in tickets_set.items():
                base_ticket = base_tickets_set[ticker]
                delta = self.calc_delta(base_ticket, ticket)
                d_open  += delta[0] * self.mixture[ticker] / 100
                d_high  += delta[1] * self.mixture[ticker] / 100
                d_low   += delta[2] * self.mixture[ticker] / 100
                d_close += delta[3] * self.mixture[ticker] / 100
            base_tickets_set = tickets_set
            output[day] = (
                round(d_open, 2),
                round(d_high, 2),
                round(d_low, 2),
                round(d_close, 2),
            )
        return output
