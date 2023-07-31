def truncate(phrase, n):
    if len(phrase) <= n:
        return phrase
    elif n <= 3:
        return phrase[:n] + '...'
    else:
        return phrase[:n-3] + '...'