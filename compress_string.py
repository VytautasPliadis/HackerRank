from __future__ import print_function
from itertools import *

for i, j in groupby(map(int, list(input()))):
    # The groupby function groups consecutive identical elements.
    # i is the key (the digit) and j is an iterator for the group of consecutive identical elements.

    # len(list(j)) calculates the length of the group, i.e., the count of consecutive identical elements.
    # This count is paired with the digit i and converted to a tuple.
    # Example: If the group is [1, 1, 1], then len(list(j)) is 3, and the tuple becomes (3, 1).
    result_tuple = tuple([len(list(j)), i])

    # The result tuple is printed, and end=" " specifies that a space should be printed at the end instead of a newline.
    print(result_tuple, end=" ")
