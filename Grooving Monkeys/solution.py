t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    c=[-1]*n
    o=[]
    s=0
    for j in range(n):
        b.append(chr(65+j))
        o.append(chr(65+j))
    while(o!=c):
        f=0
        for k in a:
            c[k-1]=b[f]
            f=f+1
        s=s+1
        c=''.join(c)
        b=list(c)
        c=list(c)
    print(s)
