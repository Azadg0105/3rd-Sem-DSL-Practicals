row=int(input("Enter no. of Rows:"))
col=int(input("Enter no. of Columns:"))
matrix=[]

#matrix function
def cmatrix():
  for i in range(row):
    a=[]
    for j in range(col):
      b=int(input())
      a.append(b)
    matrix.append(a)

  for i in range(row):
    for j in range(col):
      print(matrix[i][j],end=' ')
    print()
  return matrix

m=cmatrix()
print(m)


for i in range(row):
  for j in range(col):
    if m[i][j]==0:
      continue
    else :
      print(i,'\t',j,'\t', m[i][j])

matrix=[]
x=cmatrix()
print(x)


for i in range(row):
  for j in range(col):
    if x[i][j]==0:
      continue
    else :
      print(i,'\t',j,'\t', x[i][j])

for i in range(row):
  for j in range(col):
    if m[i][j]!=0 and x[i][j]!=0:
      print(i,'\t',j,'\t',m[i][j]+x[i][j])
