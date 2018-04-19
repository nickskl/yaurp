import datetime


def dt_to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day


def dt_from_integer(dt_int):
    result = datetime.datetime(dt_int/10000, (dt_int/100)%100, dt_int%100)
    return result