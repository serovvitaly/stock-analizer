
from collections import OrderedDict
from roost import pot
import csv_helper

mixtures = csv_helper.get_mixtures([
    'data/GAZP_130101_180222.csv',
    'data/ROSN_130101_180222.csv',
])

for year, y_items in mixtures.items():
    print(year)
    for month, m_items in y_items.items():
        print(' -', month)

pot = pot()
pot.fill_from_file('data/GAZP_130101_180222.csv')
pot.fill_from_file('data/ROSN_130101_180222.csv')


bets = {
    'GAZP': 50.05,
    'ROSN': 49.95,
}

date_from = 20160215
date_to = 20160310
for dt, data in pot.items().items():
    if dt < date_from or dt > date_to:
        continue
    ct = len(data)
    open = 0
    high = 0
    low = 0
    close = 0
    for ticker, ticket in data.items():
        bet = bets[ticker]
        open += ticket.open * bet / 100
        high += ticket.high * bet / 100
        low += ticket.low * bet / 100
        close += ticket.close * bet / 100
    open = open / ct
    high = high / ct
    low = low / ct
    close = close / ct
    #print(open, high, low, close)
