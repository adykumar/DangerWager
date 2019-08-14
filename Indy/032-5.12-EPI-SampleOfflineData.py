"""
Input: An array of elements and a size K
Output: Subset of size K from the given elements. Subsets need to be equally likely (randomly selected)

Logic:
    - Incrementally build the set of size K
    - Start with k=1 and generate a number "r" between [0 and n (n = len(A)-1)]. Swap a[0] and a[r].
    - Next for k=2, generate a number "s" between [1: len(A)-1]. Swap a[1] and a[s].
    - Repeat k times and the result is the randomly generated set
"""
from typing import List
import random


class Solution:
    def offline_sampling(self, input: List[int], k: int) -> None:
        for i in range(k):
            # generate a random int and swap that element at that index with this input[i]
            r = random.randint(i, len(input)-1)
            input[r], input[i] = input[i], input[r]

        print(input[:k])


s = Solution()
s.offline_sampling([3,7,5,11], 3)
s.offline_sampling([3,7,5,11], 4)
s.offline_sampling([3,7,5,11], 1)
s.offline_sampling([3,7,5,11], 0)
