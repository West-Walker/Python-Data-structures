def two_oldest_ages(ages):
    # Sort the ages list in ascending order
    sorted_ages = sorted(set(ages))
    
    # Get the length of the sorted_ages list
    length = len(sorted_ages)
    
    # Return the tuple (second_oldest, oldest)
    return sorted_ages[length - 2], sorted_ages[length - 1]