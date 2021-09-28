
num1 = int(input("Number of Students who play Cricket: "))
cricket = []
for i in range(num1):
    x = int(input(f"Roll Number of student {i+1} playing Cricket: "))
    cricket.append(x)
# print("Roll Numbers of Students who play Cricket: ", cricket)

num2 = int(input("Number of Students who play Badminton: "))
badminton = []
for i in range(num2):
    y = int(input(f"Roll Number of student {i+1} playing Badminton: "))
    badminton.append(y)
# print("Roll Numbers of Students who play Badminton: ", badminton)

num3 = int(input("Number of Students who play Football: "))
football = []
for i in range(num3):
    z = int(input(f"Roll Number of student {i+1} playing Football: "))
    football.append(z)
# print("Roll Numbers of Students who play Football: ", football)


# students who play both cricket and badminton

inter1 = []
for i in cricket:
    for j in badminton:
        if i == j:
            inter1.append(i)
print("Students who Play both Cricket and Badminton are: ", inter1)

# students who play either cricket or badminton but not both

def union(cricket, badminton):
    res = list(cricket)
    for i in badminton:
        if i not in cricket:
            res.append(i)
    return res

print("Students who play either Cricket or Badminton but not both: ", union(cricket, badminton))

# students who play neither cricket nor badminton

def a_not_b(cricket, badminton):
    res = list(cricket)
    for i in badminton:
        if i in res:
            res.remove(i)
        for a in res:
            return res
print("Students who play neither cricket nor badminton:", a_not_b(a_not_b(cricket,badminton),football))

# number of students who play cricket and football but not badminton

a_and_c = []
for i in cricket:
    if i not in badminton:
        a_and_c.append(i)
for i in football:
    
    if i not in badminton:
        a_and_c.append(i)
print("Number of students who play cricket and football but not badminton: ", a_not_b)