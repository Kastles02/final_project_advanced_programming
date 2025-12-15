def is_positive_number(value):
    return value.isdigit() and int(value) > 0

def valid_time(time):
    return ":" in time

def valid_date(date):
    return "/" in date
