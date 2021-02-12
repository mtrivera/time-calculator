def is_valid_day(day):
    return day.lower() in [
        'monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday'
    ]

def add_time(start, duration, start_day=None):
    start, time_of_day = start.split()
    start_hour_str, start_minute_str = start.split(':')
    start_hour = int(start_hour_str)
    start_minute = int(start_minute_str)

    duration_hour_str, duration_minute_str = duration.split(':')
    duration_hour = int(duration_hour_str)
    duration_minute = int(duration_minute_str)

    new_hour = start_hour + duration_hour

    if new_hour > 12:
        pass
    if start_minute + duration_minute > 59:
        pass

    new_minute = start_minute + duration_minute
    return str(new_hour) + ":" + str(new_minute) + ' ' + time_of_day