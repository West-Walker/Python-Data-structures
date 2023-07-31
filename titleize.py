def titleize(phrase):
    words = phrase.split()
    titleized_words = [word.capitalize() for word in words]
    return ' '.join(titleized_words)