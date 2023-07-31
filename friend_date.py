def friend_date(names, ages, hobbies):
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            if set(hobbies[i]).intersection(set(hobbies[j])):
                return True
    return False