def extract_full_name(people):
    names = []
    for person in people:
        full_name = person['first'] + ' ' + person['last']
        names.append(full_name)
    return names