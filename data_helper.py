

def calc_model_1(deltas_sets):
    res = {
        'open': {'pos_len': 0, 'pos_sum': 0, 'neg_len': 0, 'neg_sum': 0},
        'high': {'pos_len': 0, 'pos_sum': 0, 'neg_len': 0, 'neg_sum': 0},
        'low': {'pos_len': 0, 'pos_sum': 0, 'neg_len': 0, 'neg_sum': 0},
        'close': {'pos_len': 0, 'pos_sum': 0, 'neg_len': 0, 'neg_sum': 0},
    }
    deltas_sets.popitem()
    for day, delta_set in deltas_sets.items():

        if delta_set[0] > 0:
            res['open']['pos_len'] += 1
            res['open']['pos_sum'] += delta_set[0]
        else:
            res['open']['neg_len'] += 1
            res['open']['neg_sum'] += delta_set[0]

        if delta_set[1] > 0:
            res['high']['pos_len'] += 1
            res['high']['pos_sum'] += delta_set[1]
        else:
            res['high']['neg_len'] += 1
            res['high']['neg_sum'] += delta_set[1]

        if delta_set[2] > 0:
            res['low']['pos_len'] += 1
            res['low']['pos_sum'] += delta_set[2]
        else:
            res['low']['neg_len'] += 1
            res['low']['neg_sum'] += delta_set[2]

        if delta_set[3] > 0:
            res['close']['pos_len'] += 1
            res['close']['pos_sum'] += delta_set[3]
        else:
            res['close']['neg_len'] += 1
            res['close']['neg_sum'] += delta_set[3]

    res['open']['pos_sum'] = round(res['open']['pos_sum'], 2)
    res['open']['neg_sum'] = round(res['open']['neg_sum'], 2)

    res['high']['pos_sum'] = round(res['high']['pos_sum'], 2)
    res['high']['neg_sum'] = round(res['high']['neg_sum'], 2)

    res['low']['pos_sum'] = round(res['low']['pos_sum'], 2)
    res['low']['neg_sum'] = round(res['low']['neg_sum'], 2)

    res['close']['pos_sum'] = round(res['close']['pos_sum'], 2)
    res['close']['neg_sum'] = round(res['close']['neg_sum'], 2)

    return res