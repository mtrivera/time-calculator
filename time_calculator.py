def is_valid_day(day):
    return day.lower() in [
        'monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday'
    ]

def add_time(start, duration, start_day=None):
    start, time_period = start.split()

    start_hour, start_minute = map(int, start.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    runoff_minutes = 0
    runoff_hour = 0
    adjusted_hour = 0
    next_day = ''
    time_periods = { 'AM': 'PM', 'PM': 'AM'}

    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute
    current_time_period = time_period

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
           time_period = time_periods[time_period]

        # If PM changes to AM, that means the next day
        if current_time_period == 'PM' and time_period == 'AM':
            next_day = ' (next day)'

    return str(new_hour) + ":" + str(new_minute) + ' ' + time_period + next_day