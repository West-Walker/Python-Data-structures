def partition_list(lst, fn):
    passed = []
    failed = []
    for item in lst:
        if fn(item):
            passed.append(item)
        else:
            failed.append(item)
    return [passed, failed]