def flip_case(phrase, letter):
    flipped_phrase = ""
    for c in phrase:
        if c.lower() == letter.lower():
            if c.isupper():
                flipped_phrase += c.lower()
            else:
                flipped_phrase += c.upper()
        else:
            flipped_phrase += c
    return flipped_phrase
