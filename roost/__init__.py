import csv
from . import dto

class pot:

    def __init__(self):
        self.pot = {}

    def fill_from_file(self, file_name):
        # ['<TICKER>', '<PER>', '<DATE>', '<TIME>', '<OPEN>', '<HIGH>', '<LOW>', '<CLOSE>']
        with open(file_name, newline='') as fcsv:
            csv_reader = csv.reader(fcsv, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                date = int(row[2])
                ticker = row[0]
                ticket = dto.ticket(ticker, row[1], date, row[3], row[4], row[5], row[6], row[7])
                try:
                    self.pot[date][ticker].append(ticket)
                except:
                    try:
                        self.pot[date][ticker] = ticket
                    except:
                        self.pot[date] = {ticker: ticket}

    def items(self):
        return self.pot