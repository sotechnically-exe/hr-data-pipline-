def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
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
    


    
def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.
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

    