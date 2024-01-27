def greedy_algorithm(items, budget):
    # Sort items by calories/cost ratio in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info["cost"] <= budget:
            # Add item to selected items
            selected_items.append(item_name)
            total_cost += item_info["cost"]
            total_calories += item_info["calories"]

    return {"selected_items": selected_items, "total_cost": total_cost, "total_calories": total_calories}


def dynamic_programming(items, budget):
    # Create a 2D matrix of size (len(items) + 1) x (budget + 1) to store the results in
    dp_matrix = [[{"calories": 0, "cost": 0, "items": []} for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    for i, (item_name, item_info) in enumerate(items.items(), start=1):
        for j in range(budget + 1):
            if item_info["cost"] <= j:
                # Select the item if the cost is less than or equal to the budget
                if dp_matrix[i - 1][j]["calories"] < dp_matrix[i - 1][j - item_info["cost"]]["calories"] + item_info[
                    "calories"]:
                    dp_matrix[i][j]["calories"] = dp_matrix[i - 1][j - item_info["cost"]]["calories"] + item_info[
                        "calories"]
                    dp_matrix[i][j]["cost"] = dp_matrix[i - 1][j - item_info["cost"]]["cost"] + item_info["cost"]
                    dp_matrix[i][j]["items"] = dp_matrix[i - 1][j - item_info["cost"]]["items"] + [item_name]
                else:
                    dp_matrix[i][j] = dp_matrix[i - 1][j]
            else:
                dp_matrix[i][j] = dp_matrix[i - 1][j]

    return dp_matrix[len(items)][budget]


if __name__ == '__main__':
    budget = 100  # Set your budget here (can be any number)
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    greedy_result = greedy_algorithm(items, budget)
    dynamic_result = dynamic_programming(items, budget)

    print("Greedy Algorithm:")
    print("Selected Items:", greedy_result["selected_items"])
    print("Total Cost:", greedy_result["total_cost"])
    print("Total Calories:", greedy_result["total_calories"])
    print()

    print("Dynamic Programming:")
    print("Selected Items:", dynamic_result["items"])
    print("Total Cost:", dynamic_result["cost"])
    print("Total Calories:", dynamic_result["calories"])
