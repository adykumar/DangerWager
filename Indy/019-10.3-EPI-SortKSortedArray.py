"""
Input: A k-sorted array - array where an element is at most k distance away from it's actual sorted place
Output: The actual sorted array
Logic:
Since the array is k-sorted, reading k positions ensures that the smallest element in the k elements is the min element
Use a min heap to read in k elements and extract the min. Repeat until the array is exhausted.
"""
import heapq
import itertools
import collections
from typing import List
# from collections import Iterator


class Solution:
    def sort_k_sorted_array(self, input_array: List[int], k: int) -> List[int]:
        # define the min heap
        min_heap : List[int] = []

        # add first k elements to the heap
        for i in itertools.islice(input_array, k):
            heapq.heappush(min_heap, i)

        result = []
        # now iterate through the rest of the array. For every new element added, extract min and add to the result set
        for i in input_array[k:]:
            minimum = heapq.heappushpop(min_heap, i)
            result.append(minimum)

        # we have k elements left in the heap. Extract them and append to the result
        while min_heap:
            result.append(heapq.heappop(min_heap))

        return result


s = Solution()
print(s.sort_k_sorted_array([3, -1, 2, 6, 45, 8], 2))
print(s.sort_k_sorted_array([3], 2))
print(s.sort_k_sorted_array([3, -1], 2))
