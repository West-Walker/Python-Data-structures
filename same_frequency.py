def same_frequency(num1, num2):
    # Convert numbers to strings
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Check the frequency of each digit in both numbers
    freq_num1 = {}
    freq_num2 = {}
    
    for digit in str_num1:
        freq_num1[digit] = freq_num1.get(digit, 0) + 1
    
    for digit in str_num2:
        freq_num2[digit] = freq_num2.get(digit, 0) + 1
    
    # Compare the frequencies of each digit
    if freq_num1 == freq_num2:
        return True
    else:
        return False