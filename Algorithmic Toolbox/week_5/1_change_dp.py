def get_change(amount, coins=(1, 3, 4)):
    min_num_coins = [amount] * (amount + 1)
    min_num_coins[0] = 0

    for m_i in range(1, amount + 1):
        for coin in coins:
            if coin <= m_i:
                num_coins = min_num_coins[m_i - coin] + 1

                if num_coins < min_num_coins[m_i]:
                    min_num_coins[m_i] = num_coins

    return min_num_coins[amount]

if __name__ == '__main__':
    amount = int(input())
    print(get_change(amount))
