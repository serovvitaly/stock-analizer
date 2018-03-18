import csv, datetime
import mds

def get_mixtures(files_names, skeep_head=True):
    lst = {}
    for file_name in files_names:
        with open(file_name, newline='') as fcsv:
            csv_reader = csv.reader(fcsv, delimiter=',')
            if skeep_head:
                next(csv_reader)
            for row in csv_reader:
                date = datetime.datetime.strptime(row[2], '%Y%m%d').date()
                ticker = row[0]
                ticket = mds.ticket(row[4], row[5], row[6], row[7])
                if date.year not in lst:
                    lst[date.year] = {}
                if date.month not in lst[date.year]:
                    lst[date.year][date.month] = {}
                if date.day not in lst[date.year][date.month]:
                    lst[date.year][date.month][date.day] = {}
                lst[date.year][date.month][date.day][ticker] = ticket

    return lst