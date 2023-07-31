def modify_list(lst, value, location, action):
    """
    Modifies a list by removing or adding a value at the specified location.

    Parameters:
        lst (list): The input list.
        value: The value to be removed or added.
        location (str): The location where the value should be removed or added. Can be 'beginning' or 'end'.
        action (str): The action to be performed. Can be 'remove' or 'add'.

    Returns:
        If 'remove' action is performed, returns the removed value. 
        If 'add' action is performed, returns the updated list.
        If invalid commands or locations are provided, returns None.
    """
    if action == 'remove':
        if location == 'beginning':
            if len(lst) > 0:
                removed_value = lst.pop(0)
                return removed_value
        elif location == 'end':
            if len(lst) > 0:
                removed_value = lst.pop()
                return removed_value
    elif action == 'add':
        if location == 'beginning':
            lst.insert(0, value)
            return lst
        elif location == 'end':
            lst.append(value)
            return lst
    
    return None
