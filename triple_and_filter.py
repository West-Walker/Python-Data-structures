def triple_and_filter(num_list):
    result = []
    for num in num_list:
        if num % 4 == 0:
            result.append(num * 3)
    return result
