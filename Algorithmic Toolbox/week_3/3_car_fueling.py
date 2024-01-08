def calculate_min_refills(distance, tank, stations):
    stops = stations.copy()
    stops.append(distance)
    tank_left = tank

    n_refills = 0
    prev_stop = 0

    for stop in stops:
        dist = stop - prev_stop

        if dist <= tank_left:
            tank_left -= dist
        else:
            if dist > tank:
                return -1
            else:
                n_refills += 1
                tank_left = tank - dist

        prev_stop = stop

    return n_refills


if __name__ == '__main__':
    user_input_distance = int(input())
    user_input_tank = int(input())
    user_input_n_stations = int(input())
    user_input_stations = list(map(int, input().split()))

    result_min_refills = calculate_min_refills(user_input_distance, user_input_tank, user_input_stations)
    print(result_min_refills)
