def calculate_fibonacci_huge_mod(n, m):
    if n <= 1:
        return n

    remainders = [0, 1]
    period = 0

    for i in range(2, 6 * m + 2):
        remainders.append((remainders[i - 1] + remainders[i - 2]) % m)
        period += 1
        if remainders[i - 1] == 0 and remainders[i] == 1:
            break

    return remainders[n % period]


def calculate_fibonacci_sum_squares_last_digit(n):
    # Fn last digit
    fn1_ld = calculate_fibonacci_huge_mod(n, 10)
    fn2_ld = calculate_fibonacci_huge_mod(n - 1, 10)

    sum_squares_ld = fn1_ld * (fn1_ld + fn2_ld) % 10
    return sum_squares_ld


if __name__ == '__main__':
    user_input = int(input())
    result_sum_squares_last_digit = calculate_fibonacci_sum_squares_last_digit(user_input)
    print(result_sum_squares_last_digit)