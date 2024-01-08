def calculate_fibonacci(n):
    fibonacci_numbers = [0, 1]

    for i in range(2, n + 1):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])

    return fibonacci_numbers[n]


if __name__ == "__main__":
    user_input = int(input())
    result_fibonacci = calculate_fibonacci(user_input)
    print(result_fibonacci)
