def calculate_max_dot_product(sequence_a, sequence_b):
    sequence_a.sort(reverse=True)
    sequence_b.sort(reverse=True)

    result = 0

    for i in range(len(sequence_a)):
        result += sequence_a[i] * sequence_b[i]
    return result


if __name__ == '__main__':
    user_input_n = int(input())
    user_input_a = list(map(int, input().split()))
    user_input_b = list(map(int, input().split()))

    result_max_dot_product = calculate_max_dot_product(user_input_a, user_input_b)
    print(result_max_dot_product)
