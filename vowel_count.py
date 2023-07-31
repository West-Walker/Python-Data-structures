def vowel_count(phrase):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counts = {}
    for char in phrase.lower():
        if char in vowels:
            counts[char] = counts.get(char, 0) + 1
    return counts