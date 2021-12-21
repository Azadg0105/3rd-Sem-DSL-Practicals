# Write a Python program to store first year percentage of students in array.
# Write function for sorting array of floating point numbers in ascending order using
# a)Selection Sort
# b) Bubble sort and display top five scores.


# Selection Sort :
def Selec_Sort(marks):
    for i in range(len(marks)):
        min = i
        for j in range(i + 1, len(marks)):
            if marks[min] > marks[j]:
                min = j
        marks[i], marks[min] = marks[min], marks[i]

    print("Marks of Students after performing Selection Sort : ")
    for i in range(len(marks)):
        print(marks[i])

# Bubble Sort :
def Bubble_Sort(marks):
    n = len(marks)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]

    print("Marks of students after performing Bubble Sort :")
    for i in range(len(marks)):
        print(marks[i])

# Top marks :

def top_five_marks(marks):
    print("Top Five Marks are : ")
    # marks.reverse()
    # for i in range(5):
    #     print(marks[i])
    print(marks[-1:-6:-1])

 
import array as arr

marks = arr.array('i',[])
n = int(input("Enter Number of Students whose marks are to be Displayed : "))
print("Enter marks for ",n," Students: ")
for i in range(0, n):
    marks.append(int(input()))
print("The Marks of ",n," Students are : \n",marks)

rev=1
while rev==1:
    print("\nMENU")
    print("\n1. Selection Sort of the Marks")
    print("2. Bubble Sort of the Marks")
    print("3. Exit")
    ch=int(input("\nEnter your choice : "))

    if ch==1:
        Selec_Sort(marks)
        a=input("Display Top Five Marks from the List (yes/no) : ")
        if a=='yes':
            top_five_marks(marks)
        else:
            print("\nThanks for using this program..!!")
            rev=0

    elif ch==2:
        Bubble_Sort(marks)
        a=input("Display Top Five Marks from the list (yes/no) : ")
        if a=='yes':
            top_five_marks(marks)
        else:
            print("\nThanks for using this program..!!")
            rev=0

    elif ch==3:
        print("\nThanks for using this program..!!")
        rev=0

    else:
        print("\nEnter a valid choice!!")
        print("\nThanks for using this program..!!")
        rev=0
