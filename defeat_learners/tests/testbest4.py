import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

"""Test generator quality for best_4_lin_reg and best_4_dt datasets."""

import math

import numpy as np

import DTLearner as dt
import LinRegLearner as lrl
from gen_data import best_4_dt, best_4_lin_reg


def compare_os_rmse(learner1, learner2, x, y):
    """Return out-of-sample RMSE for two learners on the same split."""
    train_rows = int(math.floor(0.6 * x.shape[0]))
    train_idx = np.random.choice(x.shape[0], size=train_rows, replace=False)
    test_idx = np.setdiff1d(np.arange(x.shape[0]), train_idx)

    train_x, train_y = x[train_idx, :], y[train_idx]
    test_x, test_y = x[test_idx, :], y[test_idx]

    learner1.add_evidence(train_x, train_y)
    learner2.add_evidence(train_x, train_y)

    pred_1 = learner1.query(test_x)
    pred_2 = learner2.query(test_x)

    rmse1 = math.sqrt(((test_y - pred_1) ** 2).sum() / test_y.shape[0])
    rmse2 = math.sqrt(((test_y - pred_2) ** 2).sum() / test_y.shape[0])
    return rmse1, rmse2


def _report(label, rmse_lr, rmse_dt, expect_lr_better):
    print()
    print(f"{label} results")
    print(f"RMSE LR    : {rmse_lr}")
    print(f"RMSE DT    : {rmse_dt}")
    if expect_lr_better:
        print("LR < 0.9 DT: pass" if rmse_lr < 0.9 * rmse_dt else "LR >= 0.9 DT: fail")
    else:
        print("DT < 0.9 LR: pass" if rmse_dt < 0.9 * rmse_lr else "DT >= 0.9 LR: fail")


def test_code():
    lr_learner = lrl.LinRegLearner(verbose=False)
    dt_learner = dt.DTLearner(verbose=False, leaf_size=1)
    x, y = best_4_lin_reg()
    rmse_lr, rmse_dt = compare_os_rmse(lr_learner, dt_learner, x, y)
    _report("best_4_lin_reg()", rmse_lr, rmse_dt, expect_lr_better=True)

    lr_learner = lrl.LinRegLearner(verbose=False)
    dt_learner = dt.DTLearner(verbose=False, leaf_size=1)
    x, y = best_4_dt()
    rmse_lr, rmse_dt = compare_os_rmse(lr_learner, dt_learner, x, y)
    _report("best_4_dt()", rmse_lr, rmse_dt, expect_lr_better=False)


if __name__ == "__main__":
    test_code()

