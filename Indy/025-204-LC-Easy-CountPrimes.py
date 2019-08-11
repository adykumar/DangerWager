"""
Link: https://leetcode.com/problems/count-primes/

Input: A number N
Output: Count the number of prime numbers less than a non-negative number, n.
Example: 10, Output: 4
Logic:
- Use an array to track how many numbers from 0-N are primes. Create the array and initialize to true or 1
- Set array[0] and [1] to 0 as 0 and 1 are not primes.
- Now start with 2 and start marking all multiples (m) as false.
- To optimize and avoid repetitive checks, we check from the number's square (m^2)
- Another optimization is not checking all the way from 0 to N and stopping at sqrt(N)
"""

class Solution:
    def countPrimes(self, n: int) -> int:

        # if n<2, then return 0 and terminate
        if n < 2:
            return 0

        # array to track primes. Set status of o and 1 as false
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0

        # iterate from 0 to sqrt(N) and strike off all multiples
        for i in range(2, int(n ** 0.5)+1):
            if primes[i] != 0:
                for j in range(i*i, n, i):
                    primes[j] = 0

        return sum(primes)


s = Solution()
print(s.countPrimes(13))
