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
