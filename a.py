b=int(input("enter no:"))
a=1
n=2
print(a)
while n<=b:
    print(n,end='/')
    a=(n/(n+1))
    n=n+1
    print('=',a)
