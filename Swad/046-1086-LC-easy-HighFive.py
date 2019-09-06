"""
1086. High Five
Easy

Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

Note:

1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores
"""

"""
Time- O(n log n) for sorting
SPace- O(x) where x is number of IDs
"""

from operator import itemgetter
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        a= sorted(items, key=itemgetter(0,1))
        curr_id= a[-1][0]
        ctr= 0; Sum=0
        res= []

        for i in xrange(len(a)-1, -1, -1):
            ctr+=1
            id, val= a[i]
            if id!= curr_id:
                ctr=1
                Sum=0
                curr_id= id
            if ctr>5: continue
            Sum+= val
            if ctr==5:
                res.append([id, Sum/5])
        return res[::-1]
