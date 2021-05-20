# cython: language_level=3
from libc.stdint cimport uint64_t

cpdef uint64_t fibonacci(unsigned int n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
