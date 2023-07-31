def is_palindrome(phrase):
    # Remove spaces and convert to lowercase
    phrase = phrase.replace(" ", "").lower()
    
    # Check if phrase is equal to its reverse
    if phrase == phrase[::-1]:
        return True
    else:
        return False
