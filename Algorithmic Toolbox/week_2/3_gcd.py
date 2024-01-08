def calculate_gcd(x, y):
    if y == 0:
        return x
    x = x % y
    return calculate_gcd(y, x)

if __name__ == "__main__":
    user_input = map(int, input().split())
    num1, num2 = user_input
    result_gcd = calculate_gcd(num1, num2)
    print(result_gcd)
