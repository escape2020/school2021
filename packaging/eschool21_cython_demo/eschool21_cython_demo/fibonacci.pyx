# cython: language_level=3
import numpy as np
cimport numpy as cnp
cimport cython
from libc.stdint cimport uint64_t

cnp.import_array()

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef cnp.ndarray[uint64_t, ndim=1] fibonacci(unsigned int n):
    cdef cnp.npy_intp[1] shape = [n]
    cdef cnp.ndarray[uint64_t, ndim=1] output = cnp.PyArray_SimpleNew(1, shape, cnp.NPY_UINT64)

    output[0] = 0
    if n == 0:
        return output

    output[1] = 1

    if n == 1:
        return output

    cdef unsigned int i
    for i in range(2, n):
        output[i] = output[i - 1] + output[i - 2]

    return output
