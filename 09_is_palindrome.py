def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
# should lower case everything
# ignore spaces
# make into list and then mutate it with comprehension to get rid of spaces
# we can replace white space and then reverse with slice
    phrase = phrase.replace(" ", "").lower()
    phrase2 = phrase[::-1]

    return phrase == phrase2
    