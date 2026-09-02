import numpy as np


def calculate_rmse(observed, predicted):
    """Calculate root mean squared error."""
    observed = np.asarray(observed)
    predicted = np.asarray(predicted)
    squared_errors = (observed - predicted) ** 2
    mean_squared_error = np.mean(squared_errors)
    rmse = np.sqrt(mean_squared_error)
    return rmse


if __name__ == "__main__":
    observed = [10, 20, 30, 40]
    predicted = [12, 18, 29, 43]
    error = calculate_rmse(observed, predicted)
    print(error)

