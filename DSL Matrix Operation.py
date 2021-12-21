# A-9 Write a Python program to compute following computation on matrix:
# a)  Addition of two matrices
# b)	Subtraction of two matrices
# c)	Multiplication of two matrices
# d)	Transpose of a matrix

row = int(input("Enter no. of Rows: "))
col = int(input("Enter no. of Columns: "))

matrix1 = []

for i in range(row):
    a  = []
    for j in range(col):
        a.append(int(input("Enter Elements of First Matrix: ")))
    matrix1.append(a)
for i in range(row):
    for j in range(col):
        print(matrix1[i][j], end='  ')
    print(end='\n')

matrix2 = []

for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input("Enter Elements of Second Matrix: ")))
    matrix2.append(a)
for i in range(row):
    for j in range(col):
        print(matrix2[i][j], end='  ')
    print(end='\n')

# addition
res = []
for i in range(row):
    s = []
    for j in range(col):
        b = int(matrix1[i][j] + matrix2[i][j])
        s.append(b)
    res.append(s)

print("\nAddition of Two Matrices: ")
for i in range(row):
    for j in range(col):
        print(res[i][j], end='  ')
    print(end='\n')

# subtraction
res = []
for i in range(row):
    r = []
    for j in range(col):
        c = int(matrix1[i][j] - matrix2[i][j])
        r.append(c)
    res.append(r)

print("\nSubtraction of Two Matrices: ")
for i in range(row):
    for j in range(col):
        print(res[i][j], end='  ')
    print(end='\n')

# multiplication
result = [[0 for i in range(row)] for j in range(col)]
for i in range(row):
    for j in range(col):
        for k in range(row):
            result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]

print("\nMultiplication of Two Matrices: ")
for i in range(row):
    for j in range(col):
        print(result[i][j], end='  ')
    print(end='\n')

# transpose of two matrices
result = []
for i in range(row):
    t = []
    for j in range(col):
        trans = matrix1[j][i]
        t.append(trans)
    result.append(t)

print("\nTranspose of Matrix1: ")
for i in range(row):
    for j in range(col):
        print(result[i][j], end='  ')
    print(end='\n')

result = []
for i in range(row):
    t = []
    for j in range(col):
        trans = matrix2[j][i]
        t.append(trans)
    result.append(t)
print("Transpose of Matrix2: ")
for i in range(row):
    for j in range(col):
        print(result[i][j], end='  ')
    print(end='\n')
