# A-5 Write a Python program to compute following operations on String:
# a)	To display word with the longest length
# b)	To determines the frequency of occurrence of particular character in the string
# c)	To check given string is palindrome or not
# d)	To display index of first substring
# e)	To count the occurrences of each word in string

str = input("Enter a String: ")

# Longest length
s = str.split()
a = 0
for i in range(len(s)):
    if a < len(s[i]):
        a = len(s[i])
        b = s[i]
print(f"\nThe Longest word is '{b}' of Length {a}.")

# frequency of occurances
occ = input("\nEnter a character to find it's Frequency: ")
x = 0
for i in str:
    if i == occ:
        x += 1
    else:
        continue
print(f"Character '{occ}' occured {x} times in given String.")

# palindrome or not
pal = input("\nEnter a String to check whether Palindrome or not: ")
rev = pal[::-1]
if rev == pal:
    print("Given String is a Palindrome!")
else:
    print("Given String is not a Palindrome!")

# index of first substring
substr = input("\nEnter a Substring to find it's Position: ")
j = 0
for i in range(len(str)-1):
    if len(substr) == 0:
        break
    if str[i] == substr[j]:
        j += 1
        if j == len(substr):
            break
if j < len(substr):
    print(f"'{substr}' is not Present in a given String.")
else:
    k = i-j+1
    print(f"'{substr}' is Present at Index {k}")

# occurance of word
word = input("\nEnter a word to find its Occurance: ")
cnt = 0
for i in s:
    if i == word:
        cnt += 1
print(f"The word '{word}' occurred {cnt} time(s) in String.")
