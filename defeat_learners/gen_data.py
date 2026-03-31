"""Generate synthetic datasets that favor specific learner classes."""

import numpy as np


def best_4_lin_reg(seed=1489683273):
    """Return data where linear regression should outperform tree learners."""
    np.random.seed(seed)
    num_rows, num_features = 700, 10
    x = np.random.uniform(1, 10, size=(num_rows, num_features))

    coefficients = np.random.uniform(1, 5, size=(num_features,))
    noise = np.random.normal(0, 3, size=num_rows)
    y = np.dot(x, coefficients) + noise
    return x, y


def best_4_dt(seed=1489683273):
    """Return nonlinear data where decision trees should outperform linear regression."""
    np.random.seed(seed)
    num_rows, num_features = 700, 10
    x = np.random.uniform(1, 10, size=(num_rows, num_features))

    coefficients = np.random.uniform(1, 5, size=(num_features,))
    noise = np.random.normal(0, 3, size=num_rows)
    y = (
        coefficients[0] * x[:, 0] ** 3 * x[:, 1] ** 2
        + coefficients[1] * x[:, 0] ** 2 * x[:, 1]
        + coefficients[2] * x[:, 0] * x[:, 1] ** 2
        + coefficients[3] * x[:, 0] * x[:, 1]
        + coefficients[4] * x[:, 0]
        + coefficients[5] * x[:, 1]
        + noise
    )
    return x, y


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


if __name__ == "__main__":
    print("Synthetic dataset generator")
