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
        cout << "Yes, it is a Palindrome.";
    }
    else {
        cout << "No, it is not a Palindrome.";
    }
 
    return 0;
}
