#Python program to store marks scored by 'n' number of students in a subject
# Calculate:
# 1. Sum of marks obtained
# 2. Average score of class
# 3. Maximum and Minimum marks scored
# 4. Marks with highest Frequency


noofstud = int(input("Enter no. of students in class: "))

list1 = []
for i in range(noofstud):
    marks = int(input(f"Enter marks of Roll no. {i+1} : "))
    list1.append(marks)

#To find Sum of Marks
sum = 0
for i in range(len(list1)):
    sum = sum+list1[i]
print("Sum of marks is ", sum)

#To find Average score
sum += list1[i]
avg = sum/len(list1)
print("Average Marks obtained are: ", avg)

#Maximum marks obtained
print("Maximum marks obtained are: ", max(list1))

#Minimum marks obtained
print("Minimum marks obtained are: ", min(list1))

#To find frequent marks obtained
x = 0
res = list1[0]
for i in list1:
    freq = list1.count(i)
    if freq > x:
        x = freq
        res = i
print("Most Frequent marks is: " + str(res))