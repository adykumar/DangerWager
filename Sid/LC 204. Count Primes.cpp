/*
204. Count Primes (https://leetcode.com/problems/count-primes/)
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
*/

class Solution {
public:
    int countPrimes(int n) {     
        vector <int> arr(n+10,0);
        arr[0]=arr[1]=1;
        for(int i=2;i*i<=n;i++){
            if(arr[i]==0){
                for(int j=i*2;j<=n;j+=i){
                    arr[j]=1;
                }
            }
        }
        
        int count=0;
        for(int i=0;i<n;i++){
            if(arr[i]==0){
                count++;
            }
        }
        return count;
    }
};
