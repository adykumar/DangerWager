/*
1108. Defanging an IP Address  (https://leetcode.com/problems/defanging-an-ip-address/)
    Given a valid (IPv4) IP address, return a defanged version of that IP address.
    A defanged IP address replaces every period "." with "[.]".
    
    Example 1:
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"
*/

class Solution {
public:
    string defangIPaddr(string address) {
        string str;
        int n=address.length();
        for(int i=0;i<n;i++){
            if(address[i]=='.'){
                str=str + '[';
                str=str + address[i];
                str=str + ']';
            }
            else{
                str=str+address[i];
            }
        }
        return str;
    }
};