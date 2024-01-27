import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_simulations, num_dice):
    results = {}

    for _ in range(num_simulations):
        # Drop a few dice
        dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
        # Calculate the total sum
        total_sum = sum(dice_rolls)

        # Update the results
        if total_sum in results:
            results[total_sum] += 1
        else:
            results[total_sum] = 1

    # Calculate the probabilities
    probabilities = {k: v / num_simulations for k, v in results.items()}

    return probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probabilities_values = list(probabilities.values())

    plt.bar(sums, probabilities_values, align='center', alpha=0.7)
    plt.xlabel('Sum of dice rolls')
    plt.ylabel('Probability')
    plt.title('Probability of getting certain sum using Monte Carlo simulation')
    plt.show()


if __name__ == '__main__':
    # Set the number of simulations and the number of dice
    num_simulations = 100000
    num_dice = 2

    # Call the function to simulate dice rolls
    probabilities = simulate_dice_rolls(num_simulations, num_dice)

    # Results table
    print(f"| {'Сума чисел на кубиках':^15} | {'Ймовірність':^15} |")
    print("| --------------------- | --------------- |")
    for sum_value, probability in sorted(probabilities.items()):
        print(f"| {sum_value:^21} | {probability:15.4f} |")

    # Draw the histogram
    plot_probabilities(probabilities)
