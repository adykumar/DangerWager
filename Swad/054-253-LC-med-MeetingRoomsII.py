"""
253. Meeting Rooms II
Medium

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
"""
"""
Time- O(n log n) for n intervals  (because we sort)
Space- O(1)
"""

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        starts= []
        ends= []
        for each in intervals:
            starts.append(each[0])
            ends.append(each[1])
        starts= sorted(starts)
        ends= sorted(ends)
        i=0
        j=0
        rooms= 0
        curr= 0
        while i<len(starts):
            if starts[i]<ends[j]:
                curr+=1
                rooms= max(rooms, curr)
                i+=1
            elif starts[i]==ends[j]:
                i+=1; j+=1
            else:
                curr-=1
                j+=1
        return rooms
                    
