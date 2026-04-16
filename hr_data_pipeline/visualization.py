import os
import matplotlib.pyplot as plt


def plot_heartrate(data: list, filename: str):
    """
    My attempt at creating a simple line plot of heart-rate data.
    The image will be saved inside an 'images' folder.
    """

    # Make sure the images folder exists.
    # If not, I create it so the plot can be saved.

    if not os.path.exists("images"):
        os.makedirs("images")

    # Create the line plot.

    plt.figure(figsize=(8, 4))
    plt.plot(data, marker='o')
    plt.title("Heart Rate Over Time")
    plt.xlabel("Measurement Number")
    plt.ylabel("Heart Rate (bpm)")

    # Save the image to the images folder.

    save_path = os.path.join("images", filename)
    plt.savefig(save_path)

    # Close the plot so it doesn't stay open in memory.
    plt.close()

