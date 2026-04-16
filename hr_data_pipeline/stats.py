def average(data: list) -> float:          #Return the average of a list of numbers.Uses Python's built-in sum() and len() functions to compute: average = total of values / count of values.

    total_hr = sum(data)
    avg_of_hr = total_hr / len(data)
    return avg_of_hr

def median(data: list) -> float:

    sorted_data = sorted(data)       # sort the list so we can find the middle
    n = len(sorted_data) 
    mid = n // 2                     # integer division gives the middle index

    if n % 2 == 1:
        return sorted_data[mid]      # odd length means one middle value
    else: 
        # even length means average of the two middle values    
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    


def range(data: list) -> float: 
    return max(data) - min(data)       # Return the range of the data, which measures variability as (maximum value - minimum value)


def rolling_avg(data: list, k: int) -> float:
 """
    I wanted to give the rolling average a try.
    My understanding is that a rolling average looks at the last k values
    and finds the average of just that window. This is my attempt at it.
    """

    # I think the rolling average should use the last k numbers in the list.
    # So I'm slicing the list from the end to get that window.

 window = data[-k:]

    # I believe I should add up the values in the window.

 total = sum(window)

    # And then divide by k to get the rolling average.
    # I'm not totally sure if this is the exact formula,
    # but this is my best attempt based on what I understand.

rolling = total / k
return rolling



def variance(data: list) -> float:
    """
    My attempt at calculating variance.
    Variance measures how spread out the numbers are from the average.
    I am using the formula: average of squared differences from the mean.
    """

    # First I find the mean of the data.
    # I already wrote an average() function, so I reuse it here.
    mean = average(data)

    # I think variance should measure how far each value is from the mean.
    # So I calculate each difference and square it.

    squared_diffs = []
    for value in data:
        diff = value - mean
        squared_diffs.append(diff ** 2)

    # Then I take the average of those squared differences.
    var = sum(squared_diffs) / len(squared_diffs)


    return var



def standard_deviation(data: list) -> float:
    """
    Standard deviation is the square root of variance.
    I am using my variance() function to calculate it.
    """
    var = variance(data)
    return var ** 0.5

