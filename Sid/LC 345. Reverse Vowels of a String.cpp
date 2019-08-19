/*
345. Reverse Vowels of a String (https://leetcode.com/problems/reverse-vowels-of-a-string/)
    Write a function that takes a string as input and reverse only the vowels of a string.
    Example 1:

    Input: "hello"
    Output: "holle"
    Example 2:

    Input: "leetcode"
    Output: "leotcede"
    Note:
    The vowels does not include the letter "y".

*/



class Solution {
public:
    string reverseVowels(string s) {
        int i=0;
        int j=s.length()-1;
      while(i<j){
            if(s[i]=='a' ||s[i]=='e' ||s[i]=='i' ||s[i]=='o' ||s[i]=='u' 
               ||s[i]=='A' ||s[i]=='E' ||s[i]=='I' ||s[i]=='O' ||s[i]=='U'  ){
                if(s[j]=='a' ||s[j]=='e' ||s[j]=='i' ||s[j]=='o' ||s[j]=='u'
               ||s[j]=='A' ||s[j]=='E' ||s[j]=='I' ||s[j]=='O' ||s[j]=='U'){
                    swap(s[i++],s[j--]);
                }
                else 
                     j--;
            } 
            else    
                i++;
        }
        return s;
    }
};