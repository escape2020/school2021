def fibonacci(n):
    '''Calculate the nth fibonacci number using recursion

    Examples
    --------
    >>> fibonacci(7)
    13
    '''

    if n < 0:
        raise ValueError(f'n must be >= 0, got {n}')

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
