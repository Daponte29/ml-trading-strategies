"""Martingale betting simulation and experiment plot generation."""

import numpy as np
import matplotlib.pyplot as plt


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


def gtid():
    return 903357453


def get_spin_result(win_prob):
    """Return True for win and False for loss on one spin."""
    return np.random.random() <= win_prob


def simulator(win_prob, has_bankroll=False, bankroll=0):
    """Simulate one episode of Martingale strategy."""
    result = np.zeros(1001)
    episode_winnings = 0
    spin_idx = 0

    while spin_idx < 1001 and episode_winnings < 80:
        won = False
        bet = 1

        while not won and spin_idx < 1001:
            result[spin_idx] = episode_winnings
            spin_idx += 1
            won = get_spin_result(win_prob)

            if won:
                episode_winnings += bet
            else:
                episode_winnings -= bet
                bet *= 2

                if has_bankroll:
                    if episode_winnings <= -bankroll:
                        result[spin_idx:] = episode_winnings
                        return result
                    if episode_winnings - bet < -bankroll:
                        bet = bankroll + episode_winnings

    if spin_idx < 1001:
        result[spin_idx:] = episode_winnings

    return result


def _plot_mean_and_std(samples, title, filename):
    mean = np.mean(samples, axis=0)
    std = np.std(samples, axis=0)

    plt.axis([0, 300, -256, 100])
    plt.title(title)
    plt.xlabel("Number of Spins")
    plt.ylabel("Total Winnings")
    plt.plot(mean, label="mean")
    plt.plot(mean + std, label="mean+std")
    plt.plot(mean - std, label="mean-std")
    plt.legend()
    plt.savefig(filename)
    plt.clf()


def _plot_median_and_std(samples, title, filename):
    median = np.median(samples, axis=0)
    std = np.std(samples, axis=0)

    plt.axis([0, 300, -256, 100])
    plt.title(title)
    plt.xlabel("Number of Spins")
    plt.ylabel("Total Winnings")
    plt.plot(median, label="median")
    plt.plot(median + std, label="median+std")
    plt.plot(median - std, label="median-std")
    plt.legend()
    plt.savefig(filename)
    plt.clf()


def run_experiments(win_prob, bankroll=256):
    plt.axis([0, 300, -256, 100])
    plt.title("10 Episodes Infinite Bankroll")
    plt.xlabel("Number of Spins")
    plt.ylabel("Total Winnings")
    for _ in range(10):
        plt.plot(simulator(win_prob, False, 0))
    plt.savefig("figure1.png")
    plt.clf()

    inf_samples = np.array([simulator(win_prob, False, 0) for _ in range(1000)])
    _plot_mean_and_std(inf_samples, "1000 Episodes Infinite Bankroll", "figure2.png")
    _plot_median_and_std(inf_samples, "Median of 1000 Episodes Infinite Bankroll", "figure3.png")

    limited_samples = np.array([simulator(win_prob, True, bankroll) for _ in range(1000)])
    _plot_mean_and_std(limited_samples, f"1000 Episodes with ${bankroll} Bankroll", "figure4.png")
    _plot_median_and_std(limited_samples, f"Median of 1000 Episodes with ${bankroll} Bankroll", "figure5.png")


def test_code():
    np.random.seed(gtid())
    run_experiments(18 / 38, bankroll=256)


if __name__ == "__main__":
    test_code()
