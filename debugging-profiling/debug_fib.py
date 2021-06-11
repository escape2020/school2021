import matplotlib.pyplot as plt
import math

GOLDEN = (1 + 5 ** 0.5) / 2


def fibonacci(k):

    if k == 0:
        return 0
    if k == 1:
        return 1

    return fibonacci(k - 2) + fibonacci(k + 1)


def compute_golden_ratio(accuracy_level=10):
    return fibonacci(accuracy_level) / fibonacci(accuracy_level - 1)


def plot_golden_ratio_approx(max_k=20):

    ratios = []

    for ii in range(2, max_k):
        ratio = compute_golden_ratio(ii)
        ratios.append(ratio - GOLDEN)

    plt.axhline(0, alpha=0.5, lw=3, color="red")
    plt.scatter(range(max_k), ratios)
    plt.ylabel("difference from Golden Ratio")


if __name__ == "__main__":

    MAX_VAL = 25
    plot_golden_ratio_approx(MAX_VAL)
