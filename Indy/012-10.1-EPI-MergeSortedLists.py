"""
Input: A set of sorted sequences
Output: Union of the sequences as a single sorted sequence
Logic:
Take 1st element from each of the sorted sequences and extract min and add to the resultset
Pick the next element from this sequence and add it to the heap
After all the elements are processed, the resultset will have the final sorted list
"""
from typing import List, Tuple
import heapq

class Solution:
    def merge_sorted_arrays(self, sorted_arrays: List[List[int]]):
        # initialize the heap.
        # Heap is designed to be a pair - element and the idx of the array it came from
        heap: List[Tuple[int, int]] = []

        # Iterate through the input arrays, create the iterators
        array_iters = [iter(i) for i in sorted_arrays]

        # add first element of each input array into the heap
        for array_idx, array_iter in enumerate(array_iters):
            first_element = next(array_iter, None)
            if first_element is not None:
                heapq.heappush(heap, (first_element, array_idx))

        # extract first/smallest element and add to result set
        # add the next element from the same array the above element came from if the array is not exhausted
        # repeat until the heap/input arrays are exhausted
        result = []
        while heap:
            smallest_element, smallest_element_array_idx = heapq.heappop(heap)
            smallest_element_array_iter = array_iters[smallest_element_array_idx]
            result.append(smallest_element)
            next_element = next(smallest_element_array_iter, None)
            if next_element is not None:
                heapq.heappush(heap, (next_element, smallest_element_array_idx))

        return result


s = Solution()
print(s.merge_sorted_arrays([[3, 5, 7], [0, 6], [0, 6, 28]]))
print(s.merge_sorted_arrays([[3], [0, 6], []]))
print(s.merge_sorted_arrays([[], [], []]))
print(s.merge_sorted_arrays([[1], [1], [1]]))