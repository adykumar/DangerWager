/*
557. Reverse Words in a String III (https://leetcode.com/problems/reverse-words-in-a-string-iii/)

    Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and       initial word order.

    Example 1:
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

    Note: In the string, each word is separated by single space and there will not be any extra space in the string.

*/


class Solution {
public:
    string reverseWords(string s) {
        int i = 0, j = 0, k;
        while(j < s.size()) {
            i = j;
            while(s[j] != ' ' && j < s.size()) j++;
            k = j-1;
            while(i < k) swap(s[i++], s[k--]);
            j++;
        }
        return s;
    }
};