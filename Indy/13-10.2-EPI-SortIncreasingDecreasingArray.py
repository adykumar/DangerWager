"""
Input: A k-increasing decreasing array - an array which increases and decreases k times
Output: Final sorted array (Sorted efficiently! No O(NLogN shebang))
Logic:
The increasing/decreasing sequence can be broken into k disjoint increasing sequences by reversing the
decreasing sequences. Then they can be merged as k-sorted sequences which is O(n)
"""

from typing import List, Tuple
import heapq

class Solution():

    def merge_sorted_arrays(self, sorted_arrays: List[List[int]]):
        heap: List[Tuple[int, int]] = []

        # creating iters for subarrays
        sorted_arrays_iters = [iter(i) for i in sorted_arrays]

        # add first element form each subarray into heap
        for subarray_idx, subarray_iter in enumerate(sorted_arrays_iters):
            first_element = next(subarray_iter, None)
            if first_element is not None:
                heapq.heappush(heap, (first_element, subarray_idx))

        # extract min and add to result, add the next element from the same array to the heap
        # repeat until heap is exhausted. resultSet is the final sorted array
        result = []
        while heap:
            smallest_element, smallest_array_idx = heapq.heappop(heap)
            smallest_array_iter = sorted_arrays_iters[smallest_array_idx]
            result.append(smallest_element)
            next_element = next(smallest_array_iter, None)
            if next_element is not None:
                heapq.heappush(heap, (next_element, smallest_array_idx))
        return result

    def sort_k_increasing_decresing(self, input_array: List[int]) -> List[int]:

        # break down the array into k disjoint sorted arrays
        sorted_subarrays = []
        increasing, decreasing = range(2)  # 0 - increasing, 1 - decreasing
        subarray_type = increasing
        subarray_start_idx = 0

        # parse the array and whenever you see a reversal, reverse the array into a disjoint increasing array,
        # and add to the list of sorted arrays
        for i in range(1, len(input_array)+1):
            # check for reversal and snip off the array (reverse for decreasing arrays) and add to list of sorted arrays
            if (
                    i == len(input_array) or  # Array fully parsed
                # Example: 0, 8, 9, 12, 4, 3
                (input_array[i-1] < input_array[i] and subarray_type == decreasing) or  # reversal in decreasing array
                (input_array[i-1] >= input_array[i] and subarray_type == increasing) # reversal in increasing array
            ):
                sorted_subarrays.append(input_array[subarray_start_idx:i] if subarray_type == increasing
                                        else input_array[i-1:subarray_start_idx-1:-1])

                subarray_start_idx = i
                # switch increasing/decreasing order
                subarray_type = (decreasing if subarray_type == increasing else increasing)

        return self.merge_sorted_arrays(sorted_subarrays)


s = Solution()
print(s.sort_k_increasing_decresing([1,3,4,6,8,9,6,3,33,34,67,70,3,2,1,4,7]))
print(s.sort_k_increasing_decresing([1,1,1]))
print(s.sort_k_increasing_decresing([]))
