def intersection_lists(list1, list2):
    return list(set(list1) & set(list2)) if set(list1) & set(list2) else []