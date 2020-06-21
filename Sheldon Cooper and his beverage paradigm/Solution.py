t=int(input())
for i in range(t):
    a=[]
    n=int(input())
    for j in range(n):
        p=int(input())
        a.append(p)
    g=int(input())
    a.sort()
    f=1
    for x in range(n-2):
        y=x+1
        z=n-1
        while(y<z and f):
            if a[x]+a[y]+a[z]==g:
                print(True)
                f=0
            elif a[x]+a[y]+a[z]>g:
                z=z-1
            else:
                y=y+1
        if f==0:
            break
    if f==1:
        print(False)
                
