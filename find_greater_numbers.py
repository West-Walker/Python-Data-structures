def find_greater_numbers(numbers):
    count = 0
    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i+1]:
            count += 1
    return count