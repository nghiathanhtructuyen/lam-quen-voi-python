from collections import deque
import math
import os
import random
import re
import sys

#
# Complete the 'kFactorization' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY A
#

def kFactorization(n, A):
    # Write your code here
    A.sort()
    def helper(element, factors, A):
        if element == 1: 
            # Base condition
            factors.append(1)
            return factors
            
        if len(A) == 0:
            return [-1]
            
        # Main logic
        if element % A[-1] == 0:
            factors.append(element)
            element = element // A[-1]
        else:
            # Remove last element
            A.pop()
        return helper(element, factors, A)
    result = helper(n, [], A)
    return result[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = kFactorization(n, A)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()