def is_odd_string(word):
    positions_sum = sum(ord(c.lower()) - ord('a') + 1 for c in word)
    return positions_sum % 2 != 0