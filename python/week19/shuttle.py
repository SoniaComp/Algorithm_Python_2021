def time_to_int(t):
    h, m = [int(x) for x in t.split(':')]
    return h*60 + m


def int_to_time(t):
    h, m = divmod(i, 60)
    return f'{h:0.2d}:{m:0.2d}'


def solution(n, t, m, timetable):
    start_bus = time_to_int('9:00')
    line_up = sorted([time_to_int(t) for t in timetable])
    line_up.append(time_to_int('23:59'))

    next_crew = 0
    seat_left = 0
    cur_bus = start_bus

    for i in range(n):
        cur_bus = start_bus + t*i
        seat_left = m
        while seat_left > 0 and line_up[next_crew] <= cur_bus:
            seat_left -= 1
            next_crew += 1
    last_bus = cur_bus

    if seat_left > 0:
        return int_to_time(last_bus)
    else:
        return int_to_time(line_up[next_crew-1]-1)
