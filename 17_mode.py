def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    freq = count_freq(nums)

    max_value = max(freq.values())
    for (num, count) in freq.items():
        if count == max_value:
            return num

    # return max(freq, key=freq.get)



def count_freq(nums):
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    return counter