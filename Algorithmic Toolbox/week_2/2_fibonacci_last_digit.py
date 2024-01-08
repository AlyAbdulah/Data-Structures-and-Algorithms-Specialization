def calculate_fibonacci_last_digit(n):
    fibonacci_last_digits = [0, 1]

    for i in range(2, n + 1):
        fibonacci_last_digits.append((fibonacci_last_digits[i - 1] + fibonacci_last_digits[i - 2]) % 10)

    return fibonacci_last_digits[n]

if __name__ == "__main__":
    user_input = int()
    result_last_digit = calculate_fibonacci_last_digit(user_input)
    print(result_last_digit)
