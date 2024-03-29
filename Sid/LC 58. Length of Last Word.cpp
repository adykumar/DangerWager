/*

58. Length of Last Word(https://leetcode.com/problems/length-of-last-word/)
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
Example:
Input: "Hello World"
Output: 5

*/                        
class Solution {
public:
    int lengthOfLastWord(string s) { 
        int count = 0, length = s.length() - 1;
        while (length >= 0 && s[length] == ' ') length--;
        while (length >= 0 && s[length] != ' ') {
            count++;
            length--;
        }
        return count;
    }
};