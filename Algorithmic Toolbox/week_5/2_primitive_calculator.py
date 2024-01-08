def greedy_optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence(n):

    min_num_operations = [n] * n
    min_num_operations[0] = 0
    ops = [-1] * n
    op_types = (1, 2, 3)

    for i in range(n-1):
        for op_type in op_types:
            n_i = i + 1
            if op_type == 1:
                n_new = n_i * 2
            elif op_type == 2:
                n_new = n_i * 3
            elif op_type == 3:
                n_new = n_i + 1
            else:
                raise ValueError("New operation type {}".format(op_type))

            num_operations = min_num_operations[i] + 1
            i_new = n_new - 1

            if n_new <= n and num_operations < min_num_operations[i_new]:
                min_num_operations[i_new] = num_operations
                ops[i_new] = op_type

    seq = get_sequence(n, ops)

    return seq


def get_sequence(n, ops):
    n_seq = n
    seq = [n]
    while n_seq != 1:
        i = n_seq - 1
        op_type = ops[i]
        if op_type == 1:
            n_seq = n_seq // 2
        elif op_type == 2:
            n_seq = n_seq // 3
        elif op_type == 3:
            n_seq = n_seq - 1
        else:
            raise ValueError("New operation type {}".format(op_type))
        seq.append(n_seq)
    return seq[::-1]


def get_optimal_operations(value):
    best_num_ops = [value] * (value + 1)
    best_num_ops[0] = 0
    best_ops = [""] * (value + 1)

    for i in range(1, value + 1):
        num_ops_1 = best_num_ops[i - 1] + 1

        if i % 2 == 0:
            num_ops_2 = best_num_ops[i // 2] + 1
        else:
            num_ops_2 = value

        if i % 3 == 0:
            num_ops_3 = best_num_ops[i // 3] + 1
        else:
            num_ops_3 = value

        num_ops = [num_ops_1, num_ops_2, num_ops_3]
        cur_best_num_ops = min(num_ops)
        cur_best_num_ops_idx = num_ops.index(cur_best_num_ops)

        best_num_ops[i] = cur_best_num_ops
        if cur_best_num_ops_idx == 0:
            best_ops[i] = "+1"
        elif cur_best_num_ops_idx == 1:
            best_ops[i] = "x2"
        elif cur_best_num_ops_idx == 2:
            best_ops[i] = "x3"
        else:
            raise

    values = []
    res = value
    while res != 0:
        values.append(res)
        if best_ops[res] == "+1":
            res -= 1
        elif best_ops[res] == "x2":
            res = res // 2
        elif best_ops[res] == "x3":
            res = res // 3
        else:
            raise

    values.reverse()

    print(len(values) - 1, values)


if __name__ == '__main__':
    n = int(input())
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')

    # get_optimal_operations(n)