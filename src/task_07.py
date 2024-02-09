import numpy as np
import matplotlib.pyplot as plt


def simulate_dice_rolls_numpy(num_simulations):
    dice_rolls = np.random.randint(1, 7, size=(num_simulations, 2))
    total_sums = np.sum(dice_rolls, axis=1)

    sum_counts = np.bincount(total_sums, minlength=13)[2:]

    probabilities = sum_counts / num_simulations

    return probabilities


def display_probabilities(probabilities):
    print(" Сума    Ймовірність ")
    print("--------------------")
    for sum_val, prob in enumerate(probabilities, start=2):
        print(f"{sum_val:^6d}    {prob:.4f}")


def plot_probabilities(probabilities):
    sums = np.arange(2, 13)

    plt.bar(sums, probabilities, align='center', alpha=0.7)
    plt.xlabel('Кількість бросків кубика')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми кубиків')
    plt.xticks(sums)

    plt.show()


if __name__ == "__main__":
    num_simulations = 1000000

    probabilities = simulate_dice_rolls_numpy(num_simulations)

    display_probabilities(probabilities)

    plot_probabilities(probabilities)
