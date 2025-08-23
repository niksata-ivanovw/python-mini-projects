days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def add_time(start, duration):
    start_hour_str, rest = start.split(':')
    start_minutes, time = rest.split()
    start_minutes, start_hour = int(start_minutes), int(start_hour_str)

    duration_hour, duration_minutes = duration.split(':')
    duration_hour, duration_minutes = int(duration_hour), int(duration_minutes)

    total_start = start_hour * 60 + start_minutes
    total_duration = duration_hour * 60 + duration_minutes

    if time == 'PM':
        total_duration += 12 * 60

    end_hour, end_minutes, days_to_add = calculate_total_time(total_start, total_duration)

    if 12 <= end_hour <= 23:
        end_time = 'PM'
        end_hour -= 12
    else:
        end_time = 'AM'
    if end_hour == 0:
        end_hour = 12

    return end_hour, end_minutes, days_to_add, end_time

def calculate_total_time(total_start, total_duration):
    total_end_time = total_start + total_duration
    if total_end_time > 1440:
        days_to_add = total_end_time // 1440
        total_end_time %= 1440
        end_hour = total_end_time // 60
        end_minutes = total_end_time % 60
    elif total_end_time == 1440:
        end_hour = start_hour
        end_minutes = start_minutes
        days_to_add = 1
    else:
        end_hour = total_end_time // 60
        end_minutes = total_end_time % 60
        days_to_add = 0

    return end_hour, end_minutes, days_to_add

def main(start, duration, starting_day=False):
    if not starting_day:
        end_hour, end_minutes, days_to_add, end_time = add_time(start, duration)

        if days_to_add == 1:
            return f'{end_hour}:{end_minutes:02d} {end_time} (next day)'
        elif days_to_add > 1:
            return f'{end_hour}:{end_minutes:02d} {end_time} ({days_to_add} days later)'
        else:
            return f'{end_hour}:{end_minutes:02d} {end_time}'

    else:
        end_hour, end_minutes, days_to_add, end_time = add_time(start, duration)
        target_day = days_of_the_week[days_of_the_week.index(starting_day.lower()) + days_to_add % 7].capitalize()

        if days_to_add == 1:
            return f'{end_hour}:{end_minutes:02d} {end_time}, {target_day} (next day)'
        elif days_to_add > 1:
            return f'{end_hour}:{end_minutes:02d} {end_time}, {target_day} ({days_to_add} days later)'
        else:
            return f'{end_hour}:{end_minutes:02d} {end_time}, {target_day}'

