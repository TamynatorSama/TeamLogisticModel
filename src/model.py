import numpy as np

def logistic_model(t, K, A, r):
    """Calculate logistic growth predictions."""
    predictions = K / (1 + A * np.exp(-r * t))
    return predictions