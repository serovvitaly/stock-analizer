
from collections import OrderedDict
from roost import pot
import csv_helper
from mds import momo
import data_helper


bets = {
    'GAZP': 50.05,
    'ROSN': 49.95,
}

momon = momo(bets)

mixtures = csv_helper.get_mixtures([
    'data/GAZP_130101_180222.csv',
    'data/ROSN_130101_180222.csv',
])

for year, y_items in mixtures.items():
    for month, m_items in y_items.items():
        itms = []
        for day, d_items in m_items.items():
            itms.append(d_items)
        result = momon.get_relative_delta(m_items)
        model = data_helper.calc_model_1(result)
        if model['high']['pos_sum'] + model['high']['neg_sum'] <= 0:
            continue
        print(year, month)
        print(model['high'])
        print('\n')

