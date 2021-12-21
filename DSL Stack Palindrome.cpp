/*
A palindrome is a string of character that‘s the same forward and backward. Typically, punctuation,
capitalization, and spaces are ignored. For example, “Poor Dan is in a droop” is a palindrome, as
can be seen by examining the characters “poor danisina droop” and observing that they are the same
forward and backward. One way to check for a palindrome is to reverse the characters in the string and
then compare with them the original-in a palindrome, the sequence will be identical.
Write C++ program with functions-
1. To print original string followed by reversed string using stack
2. To check whether given string is palindrome or not
*/



#include <bits/stdc++.h>
using namespace std;
 
bool isPalindrome(string s)
{
    int length = s.size();
    stack<char> st;
 
    int i, mid = length / 2;
    for (i = 0; i < mid; i++) {
        st.push(s[i]);
    }
 
    if (length % 2 != 0) {
        i++;
    }
   
    char ele;
    while (s[i] != '\0')
    {
         ele = st.top();
         st.pop();
 
    if (ele != s[i])
        return false;
        i++;
    }
 
    return true;
}
 

int main()
{
    char s[20];
    cout<<"Enter String: ";
    cin>>s;
 
    if (isPalindrome(s)) {
        cout << "Yes, "<<s<<" is a Palindrome.";
    }
    else {
        cout << "No, "<<s<<" is not a Palindrome.";
    }
 
    return 0;
}

