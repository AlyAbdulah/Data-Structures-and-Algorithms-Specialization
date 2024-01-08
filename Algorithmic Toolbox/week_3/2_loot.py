def calculate_optimal_value(capacity, values, weights):
    total_value = 0.

    cost = [v / w for v, w in zip(values, weights)]
    sorted_indices = [i for _, i in sorted(zip(cost, range(len(cost))), reverse=True)]

    for i in range(len(cost)):
        i_sorted = sorted_indices[i]

        if capacity == 0:
            return total_value

        capacity_reduced = min(weights[i_sorted], capacity)
        capacity -= capacity_reduced
        total_value += capacity_reduced * cost[i_sorted]

    return total_value


if __name__ == "__main__":
    user_input = input()
    n, capacity = map(int, user_input.split())

    values = []
    weights = []

    for _ in range(n):
        item_values = map(int, input().split())
        v, w = item_values
        values.append(v)
        weights.append(w)

    optimal_value = calculate_optimal_value(capacity, values, weights)
    print(f"{optimal_value:.10f}")
