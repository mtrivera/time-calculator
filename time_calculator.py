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

    runoff_minutes = 0
    runoff_hour = 0
    adjusted_hour = 0
    times_of_day = { 'AM': 'PM', 'PM': 'AM'}

    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    if start_minute + duration_minute > 59:
        runoff_minutes = (start_minute + duration_minute) - 60
        runoff_hour += 1
        # If minutes is less than ten, append a leading zero
        if runoff_minutes < 10:
            new_minute = '0' + str(runoff_minutes)

    if new_hour > 12:
        adjusted_hour = new_hour + runoff_hour
        new_hour = adjusted_hour % 12

        if new_hour % 12 == new_hour:
            time_of_day = times_of_day[time_of_day]

    return str(new_hour) + ":" + str(new_minute) + ' ' + time_of_day