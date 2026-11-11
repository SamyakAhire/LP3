def fractional_knapsack(weights, values, capacity):
    items = sorted(
        zip(weights, values),
        key=lambda x: x[1] / x[0],
        reverse=True
    )

    total_value = 0

    for weight, value in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            capacity = 0

    return total_value


n = int(input("Enter number of items: "))
weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
capacity = int(input("Enter knapsack capacity: "))

print("Maximum value:", fractional_knapsack(weights, values, capacity))