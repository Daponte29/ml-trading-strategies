import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

"""Run learner assessment experiments and generate report plots."""

import math
import sys

import matplotlib.pyplot as plt
import numpy as np

import BagLearner as bl
import DTLearner as dt
import RTLearner as rt


def _load_dataset(file_path):
    data_rows = []
    with open(file_path, "r") as inf:
        for line in inf:
            try:
                values = list(map(float, line.strip().split(",")[1:]))
                data_rows.append(values)
            except ValueError:
                continue
    return np.array(data_rows)


def _split_data(data, train_ratio=0.6, seed=42):
    np.random.seed(seed)
    shuffled = np.random.permutation(data.shape[0])
    train_rows = int(train_ratio * data.shape[0])
    train_idx = shuffled[:train_rows]
    test_idx = shuffled[train_rows:]
    return (
        data[train_idx, :-1],
        data[train_idx, -1],
        data[test_idx, :-1],
        data[test_idx, -1],
    )


def _rmse(y_true, y_pred):
    return math.sqrt(((y_true - y_pred) ** 2).sum() / y_true.shape[0])


def run_experiment_1(train_x, train_y, test_x, test_y):
    rmse_in_sample = []
    rmse_out_sample = []

    for leaf_size in range(1, 21):
        learner = dt.DTLearner(leaf_size=leaf_size, verbose=False)
        learner.add_evidence(train_x, train_y)
        rmse_in_sample.append(_rmse(train_y, learner.query(train_x)))
        rmse_out_sample.append(_rmse(test_y, learner.query(test_x)))

    plt.plot(rmse_in_sample, color="blue")
    plt.plot(rmse_out_sample, color="orange")
    plt.title("RMSE vs Leaf Size for DTLearner")
    plt.xlabel("Leaf Size")
    plt.xlim(1, 20)
    plt.ylabel("RMSE")
    plt.ylim(0, 0.01)
    plt.legend(["In-Sample", "Out-Sample"], loc="best")
    plt.savefig("Q1_new_alternative_metrics.png")
    plt.close("all")


def run_experiment_2(train_x, train_y, test_x, test_y):
    rmse_in_sample = []
    rmse_out_sample = []

    for leaf_size in range(1, 21):
        learner = bl.BagLearner(
            learner=dt.DTLearner,
            kwargs={"leaf_size": leaf_size},
            bags=15,
            boost=False,
            verbose=False,
        )
        learner.add_evidence(train_x, train_y)
        rmse_in_sample.append(_rmse(train_y, learner.query(train_x)))
        rmse_out_sample.append(_rmse(test_y, learner.query(test_x)))

    plt.plot(rmse_in_sample)
    plt.plot(rmse_out_sample)
    plt.title("RMSE vs Leaf Size for BagLearner with 15 Bags")
    plt.xlabel("Leaf Size")
    plt.xlim(1, 20)
    plt.ylabel("RMSE")
    plt.ylim(0, 0.01)
    plt.legend(["In-Sample", "Out-Sample"])
    plt.savefig("Q2_new_alternative_metrics.png")
    plt.close("all")


def run_experiment_3(train_x, train_y):
    male_dt, male_rt = [], []
    mdape_dt, mdape_rt = [], []

    for leaf_size in range(1, 21):
        dt_learner = dt.DTLearner(leaf_size=leaf_size, verbose=False)
        rt_learner = rt.RTLearner(leaf_size=leaf_size, verbose=False)
        dt_learner.add_evidence(train_x, train_y)
        rt_learner.add_evidence(train_x, train_y)

        pred_dt = dt_learner.query(train_x)
        pred_rt = rt_learner.query(train_x)

        male_dt.append(np.mean(np.abs(np.log1p(train_y) - np.log1p(pred_dt))))
        male_rt.append(np.mean(np.abs(np.log1p(train_y) - np.log1p(pred_rt))))
        mdape_dt.append(np.median(np.abs((train_y - pred_dt) / train_y)))
        mdape_rt.append(np.median(np.abs((train_y - pred_rt) / train_y)))

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(male_dt)
    plt.plot(male_rt)
    plt.title("MALE for Training DTLearner vs RTLearner")
    plt.xlabel("Leaf Size")
    plt.xlim(1, 20)
    plt.ylabel("MALE")
    plt.legend(["DTLearner", "RTLearner"])

    plt.subplot(1, 2, 2)
    plt.plot(mdape_dt)
    plt.plot(mdape_rt)
    plt.title("MdAPE for Training DTLearner vs RTLearner")
    plt.xlabel("Leaf Size")
    plt.xlim(1, 20)
    plt.ylabel("MdAPE")
    plt.legend(["DTLearner", "RTLearner"])

    plt.tight_layout()
    plt.savefig("Q3_new_alternative_metrics.png")
    plt.close("all")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python testlearner.py <filename>")
        sys.exit(1)

    data = _load_dataset(sys.argv[1])
    train_x, train_y, test_x, test_y = _split_data(data)

    print(f"Train X shape: {train_x.shape}")
    print(f"Train Y shape: {train_y.shape}")
    print(f"Test X shape: {test_x.shape}")
    print(f"Test Y shape: {test_y.shape}")

    run_experiment_1(train_x, train_y, test_x, test_y)
    run_experiment_2(train_x, train_y, test_x, test_y)
    run_experiment_3(train_x, train_y)
    
    
    
    
    
    
    # # Create a learner and train it
    # learner = dtl.DTLearner(leaf_size=5, verbose=True)  # create a DTLearner
    # learner.add_evidence(train_x, train_y)  # train it
    # print(learner.author())
    
    # # Evaluate in sample
    # pred_y = learner.query(train_x)  # get the predictions
    # rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
    # print("\nIn sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=train_y)
    # print(f"corr: {c[0,1]}")
    
    # # Evaluate out of sample
    # pred_y = learner.query(test_x)  # get the predictions
    # rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    # print("\nOut of sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=test_y)
    # print(f"corr: {c[0,1]}")

