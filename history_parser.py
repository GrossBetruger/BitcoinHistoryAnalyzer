import time

from datetime import datetime


def to_stamp(time_str):
    year_month_day = time_str.split()[0]
    return int(time.mktime(datetime.strptime(year_month_day, "%Y-%m-%d").timetuple()))


def csv_reader(csv_path):
    with open(csv_path) as csv:
        return [line.strip().split(",") for line in csv.readlines()]


if __name__ == "__main__":
    for line in csv_reader("market-price.csv"):
        print(line), to_stamp(line[0])