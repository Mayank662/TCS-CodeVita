import math
n=int(input())
a = [[0 for i in range(n)] for j in range(n)]
s=0
p=[]
z=0
p.append((0,0))
for k in range(0,math.ceil(n/2)):
    i=k
    for j in range(k,n-k):
        s=s+1
        a[i][j]=s
        if a[i][j]%11==0:
            p.append((i,j))
            z=z+1
    for i in range(i+1,n-k):
        s=s+1
        a[i][j]=s
        if a[i][j]%11==0:
            p.append((i,j))
            z=z+1
    for j in range(j-1,k-1,-1):
        s=s+1
        a[i][j]=s
        if a[i][j]%11==0:
            p.append((i,j))
            z=z+1
    for i in range(i-1,k,-1):
        s=s+1
        a[i][j]=s
        if a[i][j]%11==0:
            p.append((i,j))
            z=z+1
for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()
z=z+1
print('Total Power points : ',z)
for i in p:
    print(i)
