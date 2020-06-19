x=input()
y=input()
n=input()
v=0
u=0
if x.isdigit() and y.isdigit() and n.isdigit():
    x=int(x)
    y=int(y)
    n=int(n)
    for i in range(x,y+1):
        d=0
        if i==1:
            d=1
        elif i==2:
            d=0
        else:
            for j in range(2,(i//2)+2):
                if i%j==0:
                    d=1
                    break
        if d==0:
            k=i
            num=0
            q=i
            while(q!=1 and q!=4):
                num=0
                while(k):
                    p=k%10
                    k=k//10
                    num=num+p**2
                q=num
                k=num
            if q==1:
                u=u+1
                if u==n:
                    print(i)
                    v=1
        if v==1:
            break
    if v==0:
        print('No number is present at this index')
else:
    print('Invalid input')
