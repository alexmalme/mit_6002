''' 
Exercise 3
5.0/5.0 points (graded)

Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and outputs the standard deviation of the lengths of the strings. Return float('NaN') if L is empty.

Recall that the standard deviation is computed by this equation:

∑t in X(t−μ)2N−−−−−−−−−−−−−√

where:

    μ is the mean of the elements in X.

    ∑t in X(t−μ)2 means the sum of the quantity (t−μ)2 for t in X.

    That is, for each element (that we name t) in the set X, we compute the quantity (t−μ)2. We then sum up all those computed quantities.

    N is the number of elements in X.

    Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.

    Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], stdDevOfLengths(L) should return 1.8708.

Note: If you want to use functions from the math library, be sure to import math. If you want to use numpy arrays, you should add the following lines at the beginning of your code for the grader:
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
Then, do import numpy as np and use np.METHOD_NAME in your code.
'''
import numpy as np


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L == [] or L is None:
        return np.nan
    else:
        mean = sum(len(string) for string in L) / len(L)
        std_dev = (sum((len(string) - mean) **
                       2 for string in L) / len(L)) ** 0.5
        return std_dev
