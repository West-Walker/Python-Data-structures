def most_common_number(lst):
    counter = {}
    max_count = 0
    most_common_num = None
    
    for num in lst:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
        
        if counter[num] > max_count:
            max_count = counter[num]
            most_common_num = num
    
    return most_common_num
    
