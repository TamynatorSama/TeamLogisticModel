import pandas as pd

def load_data(filename):
    """Load observation data from a CSV file."""
    data = pd.read_csv(filename)
    return data