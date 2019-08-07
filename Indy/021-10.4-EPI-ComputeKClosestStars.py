"""
Input: A coordinate system for Milky Way. Earth is (0,0,0). ~10^12 coordinates of stars stored in a file
Output: The K stars closest to earth.
Logic:
Distance can be computed using the Euclidean formula.
We use a max-heap and add the first K stars. As we add new stars, we eliminate the max from the heap i.e. the star
farther from earth. After exhausting all coordinates, you end up with the k closest stars.
Trick: k min elements => Use Max heap! And reverse.
"""

import math
import heapq
import collections
from typing import List, Tuple


# define a Star object
class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __lt__(self, other: 'Star') -> bool:
        return self.distance < other.distance


class Solution:
    def k_closest_stars(self, stars: List[Star], k: int) -> List[Star]:

        # create max heap to maintain the distance - star tuple
        max_heap: List[Tuple[float, Star]] = []

        for star in stars:

            # add star to max heap (-ve : to simulate max heap)
            heapq.heappush(max_heap, (-star.distance, star))

            # If max heap exceeds k elements, extract the max
            if len(max_heap) == k+1:
                heapq.heappop(max_heap)

        # return Star object for the k largest elements from the heap
        return[star[1] for star in heapq.nlargest(k, max_heap)]


sol = Solution()
input_stars = [Star(1,1,1), Star(1,2,4), Star(1,2,3), Star(1,2,5)]
result: List[Star] = sol.k_closest_stars(input_stars, 2)
for r in result:
    print("Star: [" + str(r.x) + ", " + str(r.y) + ", " + str(r.z) + "], Distance: " + str(r.distance))
