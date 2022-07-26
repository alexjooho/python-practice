def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    # maybe use .items, and iterate over them with the key and value
    # for(first, last) in people.items():
    # return [name for person in people for name in person.values()]  we tried our best
        #solution: return [f"{person['first']} {person['last']}" for person in people]

    #['Ada', 'Lovelace', 'Grace', 'Hopper']

   # [entry for tag in tags for entry in entries if tag in entry]

    empt = []

    for person in people:
        string =  ""
        for name in person.values():
            string += f"{name} "
        empt.append(string[:-1])
    
    return empt