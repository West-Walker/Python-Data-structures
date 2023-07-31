def count_letter(word, letter):
    count = 0
    for char in word.lower():
        if char == letter.lower():
            count += 1
    return count