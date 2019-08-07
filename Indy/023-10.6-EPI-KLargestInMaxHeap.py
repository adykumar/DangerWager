"""
Input: A max heap as array (level order traversal : L -> R)
Output: The K largest elements in the max heap
Logic: Even if the heap does not maintain full ordering of the elements, it has the property that
Any given node is at least greater than or equal to it's children nodes.
Root is the largest, followed by one of the 2 child nodes and so on.
We create a max heap of candidates and
"""

import heapq
from typing import List

class Solution:
    def k_largest_in_max_heap(self, input: List[int], k: int) -> List[int]:

        # base/edge case
        if k <= 0:
            return []

        # create a max heap of candidate elements and their positions. Add the root.
        max_candidates = []
        max_candidates.append((-input[0], 0))
        result = []

        # now parse through the k elements in the heap
        for _ in range(k):
            node_idx = max_candidates[0][1]
            result.append(-heapq.heappop(max_candidates)[0])

            # add the left child to the candidates
            left_child_idx = 2*node_idx + 1
            if left_child_idx < len(input):
                heapq.heappush(max_candidates, (-input[left_child_idx], left_child_idx))

            # add the right child to the candidates
            right_child_idx = 2*node_idx + 2
            if right_child_idx < len(input):
                heapq.heappush(max_candidates, (-input[right_child_idx], right_child_idx))

        # loop exits once we have parsed and extracted k elements
        # max heap ensures the running max is always on the 0th position and extract using the heappop
        return result


s = Solution()
print(s.k_largest_in_max_heap([561,314,401,28,156,359,271,11,3], 4))