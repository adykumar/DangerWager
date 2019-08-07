"""
295. Find Median from Data Stream
Hard

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.
For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

Example:
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

Follow up:
If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""

"""
Time- n log n
Space- n
"""

from heapq import heappush as hpush  #minheap
from heapq import heappop as hpop

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lh= []
        self.rh= []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.lh==[] or -self.lh[0]>=num:
            hpush(self.lh, -num)
        else:
            hpush(self.rh, num)
        if len(self.lh)>len(self.rh):
            hpush(self.rh, -hpop(self.lh))
        if len(self.lh)<len(self.rh):
            hpush(self.lh, -hpop(self.rh))



    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lh)==len(self.rh):
            return 0.5*(-self.lh[0]+self.rh[0])
        if len(self.lh)>len(self.rh):
            return -self.lh[0]
        return self.rh[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
