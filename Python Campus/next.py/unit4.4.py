def gen_secs():
    sec_gen = (sec for sec in range(0, 60))
    return sec_gen

def gen_minutes():
    min_gen = (min for min in range(0, 60))
    return min_gen

def gen_hours():
    hour_gen = (hour for hour in range(0, 24))
    return hour_gen

def gen_time():
    for hour in gen_hours():
        for min in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, min, sec)

def gen_years(start=2016):
    while True:
        yield start
        start += 1

def gen_months():
    month_gen = (month for month in range(1, 13))
    return month_gen

def gen_days(month, leap_year=True):

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return (day for day in range(1, 32))
    if month == 4 or month == 6 or month == 9 or month == 11:
        return (day for day in range(1, 31))
    if month == 2 and leap_year == True:
        return (day for day in range(1, 30))
    if month == 2 and leap_year == False:
        return (day for day in range(1, 29))

def check_if_leap (year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def gen_date():
    for year in gen_years():
        condition = check_if_leap(year)
        for month in gen_months():
            for day in gen_days(month, condition):
                for time in gen_time():
                    yield "%02d/%02d/%02d" % (year, month, day) + " " + time

i=0
gt = gen_date()
while True:
    if i%1000000==0:
        print(next(gt))
    else:
        next(gt)
    i=i+1


