import csv
import sys


def load_dates(path):
    f1 = open(path, 'r')
    datastore = {
        dates[1]
        .lower()
        .strip()
        .replace('-', ' '): {
            dates[3].lower().strip(),
            dates[4].lower().strip().replace('-', ' '),
        }
        for dates in csv.reader(
            f1.readlines(),
            quotechar='"',
            delimiter=',',
            quoting=csv.QUOTE_ALL,
            skipinitialspace=True,
        )
        if len(dates) == 5
        and dates[1].lower().strip() != ''
        and dates[0].lower().strip() != ''
        and dates[2].lower().strip() != ''
        and dates[2].lower().strip() != ''
    }
    print("Number of dates loaded: ", len(datastore))
    return datastore


def load_external_resources(resource_dir = './'):
    print(sys.path)
    return {'date': load_dates(f'{resource_dir}Dates.csv')}


if __name__ == '__main__':
    ext_KB = load_external_resources()
