def is_valid_day(day):
    return format_day(day) in [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]


def get_new_day(start_day, days_passed):
    days = [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]
    new_day_index = (days.index(format_day(start_day)) + days_passed) % 7
    return days[new_day_index]


def format_day(day):
    return day[0].upper() + day[1:].lower()


def update_time_period(days):
    time_periods = ['AM', 'PM']
    new_time_period_index = days % 2
    return time_periods[new_time_period_index]


def add_time(start, duration, start_day=None):
    start, time_period = start.split()
    start_hour, start_minute = map(int, start.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # If no duration value, return the original start time and time period
    if duration_hour == 0 and duration_minute == 0:
        if start_minute < 10:
            start_minute = '0' + str(start_minute)
        return f'{str(start_hour)}:{str(start_minute)} {time_period}'

    runoff_hour = 0
    next_day = ''
    new_day = ''
    time_periods = {'AM': 'PM', 'PM': 'AM'}

    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute
    new_time_period = ''

    if start_minute + duration_minute > 59:
        runoff_minutes = (start_minute + duration_minute) - 60
        runoff_hour += 1
        # Use case for period change at 12
        if (runoff_hour + new_hour) % 12 == 0:
            new_hour = 12
            time_period = time_periods[time_period]
        # If minutes is less than ten, append a leading zero
        if runoff_minutes < 10:
            new_minute = '0' + str(runoff_minutes)

    # If larger than 24 hours, calculate the amount of days passed
    day_count = round((start_hour + duration_hour + runoff_hour) / 24)

    if new_hour > 12:
        adjusted_hour = new_hour + runoff_hour
        new_hour = adjusted_hour % 12

        if new_hour % 12 == new_hour:
            new_time_period = time_periods[time_period]
            # If more than 24 hours, reset new time period, and use the start time period
            if duration_hour >= 24:
                new_time_period = ''

        # If time period changes, that means the next day
        if new_time_period == 'AM' and time_period == 'PM' or duration_hour >= 24:
            next_day = ' (next day)'

    # If days is more than one, update next day string
    if day_count > 1:
        next_day = f' ({day_count} days later)'
        time_period = update_time_period(day_count)

    # If start day is valid get the new day
    if start_day and is_valid_day(format_day(start_day)):
        new_day = f', {format_day(get_new_day(start_day, day_count))}'

    # If time period changed update the original time period
    if new_time_period:
        time_period = new_time_period

    return f'{str(new_hour)}:{str(new_minute)} {time_period}{new_day}{next_day}'
