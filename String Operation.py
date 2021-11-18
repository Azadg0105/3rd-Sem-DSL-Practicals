element = input("Enter the String: ")
char=input("Enter the character whose occurence you want to find: ")
count=0
counter=0
# To check length of string
for i in range(len(element)):
  count=count+1
print("Length of string:",count)
print()
# occurence of Character in string
counter=0
for i in range(len(element)):
  if char==element[i]:
    counter+=1
print("occurence of Character in string:",counter)
print()
# STRING IS PALINDROME OR NOT
if (element  == element [::-1]):
 print("The given string is palindrome")
else:
 print("The given string is not palindrome")
print()
# find word with longest length
element2=input("Enter string to find word with longest length:")
list=element2.split()
z=0
for i in range(len(list)):
  len(list[i])
  if z< len(list[i]):
    z=len(list[i])
    word=i
print("\nThe Word With Longest Length is:", list[word])
print()
#occurence of word
element3=input(" Enter string to count occurence of word :")
total=dict()
words=element3.split()
for i in words:
  if i in total:
    total[i]+=1
  else:
    total[i]=1
print(total)
print()
#To display index of first appearance of substring
element4=input(" Enter string to display index of first appearance of substring:")
element5=input(" Enter substring:")
sublen=len(element5 )
x=0
y=0
for i in range(len(element4)):
  if element5[y]==element4[i]:
    sub=1
    y=y+1
    if y==sublen:
      x=i-(sublen-1)
      break
  else:
     sub=0
     y=0
print("index of sunstring is:",x)