"""
973. K Closest Points to Origin
Medium

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""

"""
Time- n log k (log n is insertion time in heap)
Space- k
QUICK SELECT can provide a faster approach than using heaps
"""

from heapq import heappush as push
from heapq import heappop as pop
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap= []
        for x,y in points[:K]:
            push(heap, (-x**2-y**2, x, y))
        for x,y in points[K:]:
            push(heap, (-x**2-y**2, x, y))
            pop(heap)
        res= []
        while len(heap)>0:
            x= pop(heap)
            res.append([x[1], x[2]])
        return res

        
