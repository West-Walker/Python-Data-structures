def sum_range(start=0, end=None):
    if end is None:
        end = start
        start = 0
    return sum(range(start, end+1)
