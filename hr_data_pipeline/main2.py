def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    """
    This function loops through each item in the input list and tries to convert
    it into an integer. If the conversion fails (for example, if the value is a
    word or symbol), I add it to the `removed` list because it cannot be used
    for calculations.

    If the value *can* be converted to an integer, I then check whether it falls
    within a realistic human heart-rate range (30 to 250 bpm). Values outside
    this range are also added to `removed`.

    All valid values are added to the `cleaned` list. At the end, the function
    returns both lists so I can measure data quality later.

    I originally got stuck on why we use `.append()`. I learned that
    lists need methods like `.append()` to add items, and writing something like
    `removed(value)` is not valid Python because lists are not functions.
    """

    cleaned = []   # will store only valid heart-rate values
    removed = []   # will store invalid or unrealistic values

    for value in data:
        
        # Try converting the value to an integer.
        # If it fails, the value is not a number and must be removed.
        try:
            v = int(value)
        except:
            removed.append(value)  # add the bad value to the removed list
            continue               # skip the rest of this loop iteration

        # Check if the number is within a realistic heart-rate range.
        if 30 <= v <= 250:
            cleaned.append(v)      # valid, keep it
        else:
            removed.append(value)  # unrealistic, remove it

    return cleaned, removed
    

def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    """
    I am not using Python's built-in sum() function because the assignment
    wants me to practice looping and manually adding values. I loop through
    the list, add each number to a running total, and count how many numbers
    I have seen. Then I divide total by count.

    I added a check to avoid dividing by zero in case the list is empty.
    """

    total = 0   # running sum of all numbers
    count = 0   # how many numbers we've seen

    for num in data:
        total += num   # add the number to the total
        count += 1     # increase the count by one

    # Avoid division by zero if the list is empty.
    return total / count if count > 0 else 0

def median(data: list) -> float:
    
    """
    Calculate the median (middle value) of a list of integers.

    First, I sort the list because the median only makes sense when the values
    are in order. If the list has an odd number of elements, the median is the
    single middle value. If the list has an even number of elements, the median
    is the average of the two middle values.

    I got stuck at first understanding why sorting is necessary, but I realized
    that without sorting, the "middle" value would be meaningless.
    """

    sorted_data = sorted(data)  # sort the list so we can find the middle
    n = len(sorted_data)
    mid = n // 2                # integer division gives the middle index

    if n % 2 == 1:
        return sorted_data[mid]  # odd length means one middle value
    else:
        # even length means average of the two middle values
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2 


def range(data: list) -> float:

    """
    Calculate the range of a list of integers.

    The range is the difference between the largest and smallest values.
    Python already has built-in functions max() and min(), so this function
    is short. I originally thought I needed a loop, but using max/min is the
    simplest and most readable solution.
    """

    return max(data) - min(data)


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    
    """
    Read heart-rate data from a file, clean it, and calculate summary statistics.

    This function handles the full workflow:
    1. Open the file and read each line into a list.
    2. Clean the data using clean_heartrate_data().
    3. Calculate the average, median, and range using the functions I wrote.
    4. Print out data quality information and final statistics.

    I originally got stuck on how to properly read a file. I learned that using
    'with open(...) as f:' is the safest way because it automatically closes the
    file for me. I also learned that I need to strip newline characters and skip
    empty lines before adding values to the list.
    """


    data = []  # will store raw values from the file as strings

    # open file using file I/O and read it into the `data` list
    with open(file, "r") as f:
        for line in f:
            line = line.strip()   # remove spaces and newline characters
            if line:              # skip empty lines
              data.append(line) # store the raw value in the list

    # Use `clean_heartrate_data` to clean the data and remove invalid entries

    cleaned_list, removed_values = clean_heartrate_data(data)

    # calculate the average, median, and range of this file using the functions you've wrote
    avg = average(cleaned_list)
    med = median(cleaned_list)
    ran = range(cleaned_list)

    
    # print out your data quality measure to the console

    # print out your descriptive statistics to the console
 
    """ 
    I got stuck here because I wasn't sure exactly what format to use.I know I need to use cleaned_list and removed_values.
    I also know I need to print out the average, median, and range. I just wasn't sure how to format it all together in a way that is clear and readable.
    """





if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
