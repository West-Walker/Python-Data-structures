def includes(collection, sought, start=None):
    if isinstance(collection, (list, str, tuple)):
        if start is not None:
            return sought in collection[start:]
        else:
            return sought in collection
    elif isinstance(collection, set):
        return sought in collection
    elif isinstance(collection, dict):
        return sought in collection.values()
    else:
        return False