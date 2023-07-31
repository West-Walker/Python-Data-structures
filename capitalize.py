def capitalize_first_word(phrase):
    words = phrase.split()  # split the phrase into words
    if words:  # check if there are any words
        words[0] = words[0].capitalize()  # capitalize the first word
    return ' '.join(words)  # join the words back into a phrase
