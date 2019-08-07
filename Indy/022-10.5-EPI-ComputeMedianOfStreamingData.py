"""
Input: A sequence of numbers in a streaming fashion
Output: Running median of the sequence
Logic:
Use two heaps - a max heap for the smaller half and a min heap for the larger half.
We maintain an invariant to keep the heaps balanced (same number of elements or difference of at max 1)
Adding a new element can lead to largest element of the min heap move to the max heap or
smallest element of the max heap move to the min heap
"""

import heapq
# import collections
from typing import List

class Solution:
    def streaming_median(self, sequence: List[int]) -> List[float]:

        # create 2 heaps - min heap to store the larger half and max heap to store the smaller half
        min_heap: List[int] = []
        max_heap: List[int] = []
        running_median = []

        # read values from the stream. Add them to a heap while ensuring balance of the two heaps
        for i in sequence:
            heapq.heappush(max_heap, -heapq.heappushpop(min_heap, i))

            # if heap sizes differ, re-balance
            if len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

            # calculate the current median
            running_median.append(0.5*(min_heap[0] + (-max_heap[0])) if len(min_heap) == len(max_heap) else min_heap[0])

        return running_median


s = Solution()
print(s.streaming_median([1,0,3,5,2,0,1]))