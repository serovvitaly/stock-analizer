import datetime

class ticket:

    def __init__(self, ticker, per, date, time, open, high, low, close):
        #try:
            self.ticker = ticker
            self.per = per
            self.date = datetime.datetime.strptime(str(date), '%Y%m%d').date()
            self.time = datetime.datetime.strptime(time, '%H%M%S').time()
            self.open = float(open)
            self.high = float(high)
            self.low = float(low)
            self.close = float(close)
        #except ValueError:
        #    pass
