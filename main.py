from src.data import load_data
from src.model import logistic_model
from src.metrics import calculate_rmse
from src.visualization import plot_model

data = load_data("data/observations.csv")

K = 1000
A = 20
r = 0.4

predictions = logistic_model(data["day"], K, A, r)
rmse = calculate_rmse(data["customers"], predictions)

print(f"Root Mean Squared Error: {rmse:.2f}")
plot_model(data, predictions)
