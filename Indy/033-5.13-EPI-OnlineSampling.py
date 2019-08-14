"""
Input: A stream of values (network packets) and an integer k
Output: A program that maintains a uniform random subset of size k

Logic:
    - We generate the first K-set by randomly choosing k samples from N.
    - For the (n+1) packet:
        - it should be in the subset with k/(n+1) probability.
        - we chose an existing packet to remove from the subset randomly
        - the resulting k-subset is a random subset selected from n+1 elements
"""
from typing import List, Iterator
import itertools
import random


class Solution:
    def online_random_sampling(self, stream: Iterator[int], k: int) -> List[int]:

        # first create the first k-subset by taking k elements from the stream
        running_subset = list(itertools.islice(stream, k))

        samples_seen_so_far = k
        for sample in stream:
            samples_seen_so_far += 1
            idx_to_replace = random.randrange(samples_seen_so_far)

            # if the randomly generated idx to replace is < k, replace an existing element from the subset
            if idx_to_replace < k:
                running_subset[idx_to_replace] = sample

        return running_subset


s = Solution()
print(s.online_random_sampling([2,4,5,1,3,6,11,0,8,81,26,44], 5))
print(s.online_random_sampling([2,4,5,1,3,6,11,0,8,81,26,44], 1))
print(s.online_random_sampling([2,4,5,1,3,6,11,0,8,81,26,44], 0))
print(s.online_random_sampling([2,4,5], 3))


