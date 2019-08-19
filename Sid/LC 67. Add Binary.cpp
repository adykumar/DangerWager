/*
67. Add Binary (https://leetcode.com/problems/add-binary/)

Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
*/

//Easy solution video : (https://www.youtube.com/watch?v=cwRCdVVPxek)
class Solution {
public:
    string addBinary(string a, string b) {
        
        string result="";
        int carry = 0;
        int i=a.size()-1;
        int j=b.size()-1;
        
        while(i>=0 || j>=0 || carry==1){
            if(i>=0){
                carry+=a[i]-'0';
            }else{
                carry+=0;
            }
            
            if(j>=0){
                carry+=b[j]-'0';
            }else{
                carry+=0;
            }
            
            result=char((carry%2)+'0')+result;
            carry/=2;
            i--;j--;   
        }
   return result;
    }
};