def calculate_change(coins):
    coin_types = [10, 5, 1]
    coin_types.sort(reverse=True)
    coin_count = 0

    while coins != 0:
        current_coin = coin_types[0]

        if coins >= current_coin:
            first_coin_count = coins // current_coin
            coin_count += first_coin_count

            coins -= first_coin_count * current_coin

        coin_types = coin_types[1:]
    return coin_count


if __name__ == '__main__':
    user_input = int(input())
    result_change = calculate_change(user_input)
    print(result_change)
