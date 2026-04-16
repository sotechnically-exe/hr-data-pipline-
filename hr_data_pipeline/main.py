import stats
from clean.py import clean_heartrate_data
from visualization import plot_heartrate


def run(file: str):
    """
    Process heart-rate data from a file by:
      - reading raw values
      - cleaning the data
      - calculating summary statistics
      - generating a line plot
    """

    data = []

    # Read raw values from the file
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(line)

    # Clean the data
    cleaned_list, removed_values = clean_heartrate_data(data)

    # Calculate statistics using the stats module
    list_avg = stats.average(cleaned_list)
    list_med = stats.median(cleaned_list)
    list_ran = stats.range(cleaned_list)
    list_var = stats.variance(cleaned_list)
    list_std = stats.standard_deviation(cleaned_list)

    # Print results
    print(f"\n--- Results for {file} ---")
    print("Removed values:", removed_values)
    print("Average:", list_avg)
    print("Median:", list_med)
    print("Range:", list_ran)
    print("Variance:", list_var)
    print("Standard Deviation:", list_std)

    # Save plot
    plot_heartrate(cleaned_list, f"{file}_plot.png")


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
