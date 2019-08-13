"""
Input: 2 arrays representing integers
Output: Their product

Logic:
- We simulate multiplication digit by digit
- If num1 is m digits and num2 is n digits, product will at max by n+m digits
- We evaluate result as: (start with LSB i.e. reverse)
- 123 * 234 = 4*123 + 3*10*123 + 2*100*123
"""

from typing import List


class Solution:
    def multiply(self, num1: List[int], num2: List[int]) -> List[int]:
        # save the sign of the final result and make the numbers positive
        sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
        num1[0], num2[0] = abs(num1[0]), abs(num2[0])

        # allocate result array
        result = [0] * (len(num1) + len(num2))

        # evaluate the result digit by digit
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                result[i+j+1] += num1[i] * num2[j]
                result[i+j] += result[i+j+1]//10
                result[i+j+1] %= 10

        # check for leading zeros and remove if any (eg: mul by 0 will result in m+n number of zeros)
        result = result[next((i for i, x in enumerate(result) if x != 0),
                             len(result)):] or [0]

        # add the sign back to the array and return
        return [sign*result[0]] + result[1:]

s = Solution()
print(s.multiply([1,2,3], [9,8,7]))
print(s.multiply([1,2,3], [0]))
print(s.multiply([1,2,3], [0,0,0]))
print(s.multiply([-1,2,3], [0,1]))
print(s.multiply([-0,0,0,2], [0,0,1]))
