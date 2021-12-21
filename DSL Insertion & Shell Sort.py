# Write a Python program to store second year percentage of students in array.
# Write function for sorting array of floating point numbers in ascending order using
# a) Insertion sort
# b) Shell Sort and display top five scores

def insertion_sort(sort_list):
    # key = arr.array('i', [])
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key < sort_list[j]:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
    print("\nPercentage of Students by Insertion Sort: ")
    for i in range(len(sort_list)):
        print(sort_list[i])

def shellsort(arr,n):
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while(j>=gap and arr[j-gap]>temp):
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=temp
        gap=gap//2
    print("Percentage of Students by Shell Sort: ")
    for i in range(len(arr)):
        print(arr[i])

def top_five_marks(s):
    print("Top Five Marks are : ")
    # marks.reverse()
    # for i in range(5):
    #     print(marks[i])
    print(s[-1:-6:-1])

import array as arr

n=int(input("Enter Total number of students: "))
s=arr.array('i',[])
print(f"Enter Percentage of {n} Students: ")
for i in range(n):
    s.append(int(input()))

rev=1
while rev==1:
    print("\n             MENU")
    print("\n1. Insertion Sort of the Percentage")
    print("2. Shell Sort of the Percentage")
    print("3. Exit")
    ch=int(input("\nEnter your choice : "))

    if ch==1:
        insertion_sort(s)
        a = input("\nDisplay Top Five Percentage from the List (yes/no) : ")
        if a=='yes':
            top_five_marks(s)
        else:
            print("\nThanks for using this program..!!")
            rev=0
    elif ch==2:
        shellsort(s,len(s))
        a = input("\nDisplay Top Five Percentage from the list (yes/no) : ")
        if a=='yes':
            top_five_marks(s)
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


