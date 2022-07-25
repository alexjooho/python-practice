def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if len(lst) == 0:
        return None
    return lst.pop()

    # could also just do lst[-1] to slice the last item, it will return none if the list is empty