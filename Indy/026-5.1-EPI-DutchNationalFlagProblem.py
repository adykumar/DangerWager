"""
Input: An array A and an index i
Output: Re-arranged array A' so that all elements < A[i] appear first, then elements = A[i] and finally > A[i]

Logic:
- This is the partitioning step of quick sort.
- Use 3 pointers : smaller, equal and larger. Equal keeps track of the elements being classified.
- Compare each element with the pivot and if:
    - It's smaller, exchange smaller and equal (basically move smaller element to the front). Advance both.
    - It's equal, noop. Advance equal
    - It's larger, exchange larger and equal and reduce the larger pointer.
"""

from typing import List


class Solution:
    def dutch_national_flag(self, A: List[int], pivot_idx: int) -> None:
        pivot = A[pivot_idx]
        smaller, equal, greater = 0, 0, len(A)-1

        while equal < greater:
            if A[equal] < pivot:
                A[smaller], A[equal] = A[equal], A[smaller]
                smaller, equal = smaller+1, equal+1
            elif A[equal] == pivot:
                equal += 1
            else: # A[equal] > pivot
                A[equal], A[greater] = A[greater], A[equal]
                greater -= 1

        print("Pivot element: " + str(pivot) + " | Final array: " + str(A))


s = Solution()
s.dutch_national_flag([0,1,2,0,-2,-1,1], 3)
s.dutch_national_flag([0,-1,-2,0,-2,-1,1], 6)
s.dutch_national_flag([0,1], 1)
