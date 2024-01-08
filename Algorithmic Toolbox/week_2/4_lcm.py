def calculate_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def calculate_lcm(a, b):
    if a == b == 0:
        return 0
    return a * b // calculate_gcd(a, b)

if __name__ == '__main__':
    user_input = map(int, input().split())
    num1, num2 = user_input
    result_lcm = calculate_lcm(num1, num2)
    print(result_lcm)
