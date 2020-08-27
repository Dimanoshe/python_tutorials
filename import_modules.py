import datetime

year, month, day = (int(i) for i in(input()).split())
next = int(input())


def next_date(year, month, day, next):
    date = datetime.date(year, month, day)
    date += datetime.timedelta(next)
    print(date.year, date.month, date.day)


next_date(year, month, day, next)