import numpy as np


def calculate_rmse(observed, predicted):
    """Calculate root mean squared error."""
    observed = np.asarray(observed)
    predicted = np.asarray(predicted)
    squared_errors = (observed - predicted) ** 2
    mean_squared_error = np.mean(squared_errors)
    rmse = np.sqrt(mean_squared_error)
    return rmse
