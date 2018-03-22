import time

from datetime import datetime


def to_stamp(time_str):
    year_month_day = time_str.split()[0]
    return int(time.mktime(datetime.strptime(year_month_day, "%Y-%m-%d").timetuple()))


def csv_reader(csv_path):
    with open(csv_path) as csv:
        return [line.strip().split(",") for line in csv.readlines()]


def to_dataset(csv_path):
    raw = csv_reader(csv_path)
    return [(to_stamp(raw_time), float(raw_price)) for raw_time, raw_price in raw]


if __name__ == "__main__":
    for data_point in to_dataset("market-price.csv"):
        print(data_point)