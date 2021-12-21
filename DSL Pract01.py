# A-2 Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students
# in the class. Write functions to compute following:
# a)	The average score of class
# b)	Highest score and lowest score of class
# c)	Count of students who were absent for the test
# d)	Display mark with highest frequency

noofstud = int(input("Enter Number of Students in Class: "))
list1 = []
for i in range(noofstud):
    list1.append(int(input((f"Enter marks of Roll No.{i+1} (-1 for absent): "))))

# Remove absents from list
marks = []
absent = []
for i in list1:
    if i != -1:
        marks.append(i)
    else:
        absent.append(i)

# average score
sum = 0
for i in list1:
    sum += i
avg = sum/len(marks)
print("\nAverage Score of Class: ",avg)

# Maximum and Minimum 
max = 0
min = marks[0]
for i in marks:
    if i > max:
        max = i
    elif i < min:
        min = i
print("\nHighest Score of Class: ", max)
print("Lowest Score of Class: ", min)

print("\nNumber of Students absent for test: ", absent.count(-1))

# Highest frequency
x = 0
freq = marks[0]
for i in marks:
    temp = marks.count(i)
    if temp > x:
        freq = i
        x = temp
print("\nMarks with Highest Frequency: ",freq)
