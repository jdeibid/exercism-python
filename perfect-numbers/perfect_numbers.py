def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Check for nevatige numbers.
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')
    divisors = list()
    # Create a list of divisors.
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    # Check for perfect numbers.
    if sum(divisors) == number:
        return "perfect"
    elif sum(divisors) > number:
        return "abundant"
    else:
        return "deficient"