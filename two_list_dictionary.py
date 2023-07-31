def two_list_dictionary(keys, values):
    dictionary = {}

    for i in range(len(keys)):
        if i < len(values):
            dictionary[keys[i]] = values[i]
        else:
            dictionary[keys[i]] = None

    return dictionary