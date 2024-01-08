def calculate_optimal_summands(number):
    summands = []
    p = 1

    while number > 0:
        number -= p
        if (p + 1) > number:
            p_last = p + number
            summands.append(p_last)
            number = 0
        else:
            summands.append(p)
            p += 1
    return summands


if __name__ == '__main__':
    user_input = int(input())
    result_optimal_summands = calculate_optimal_summands(user_input)

    print(len(result_optimal_summands))
    for x in result_optimal_summands:
        print(x, end=' ')
