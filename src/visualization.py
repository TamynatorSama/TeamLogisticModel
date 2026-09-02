import matplotlib.pyplot as plt
def plot_model(data, predictions):
    """Plot observed data and logistic model predictions."""
    plt.figure(figsize=(8, 5))
    plt.scatter(data["day"], data["customers"], label="Observed Data")
    plt.plot(data["day"], predictions, label="Logistic Model")
    plt.xlabel("Day")
    plt.ylabel("Number of Customers")
    plt.title("Observed Data and Logistic Model")
    plt.legend()
    plt.grid(True)
    plt.savefig( "model_plot.png", dpi=300, bbox_inches="tight" )
    plt.close()

if __name__ == "__main__":
    import pandas as pd
    test_data = pd.DataFrame({
    "day": [0, 1, 2, 3, 4],
    "customers": [50, 70, 110, 170, 250]
    })
    test_predictions = [48, 75, 115, 175, 245]
    plot_model(test_data, test_predictions)