/*
344. Reverse String(https://leetcode.com/problems/reverse-string/ )

    Write a function that reverses a string. The input string is given as an array of characters char[].
    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.You     may assume all the characters consist of printable ascii characters.
    Example 1:

    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
*/

class Solution {
public:
    void reverseString(vector<char>& s) {
        int i=0;
        int j=s.size()-1;
        while(i<j){
            swap(s[i++],s[j--]);
            
        }
        
    }
};