def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    # start with sum = 0
    # loop over nums and do isinstance to see if it is a float

    sum = 0

    for num in nums:
        if isinstance(num, float):
            sum += num

    return sum

    #solution: return sum([num for num in nums if isinstance(num, float)])
    # make a list with comprehension of all nums that are floats, and then sum it