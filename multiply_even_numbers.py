def multiply_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    if len(even_numbers) == 0:
        return 1
    else:
        result = 1
        for num in even_numbers:
            result *= num
        return result