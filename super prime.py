from math import*
def proper(n):
    if n==1:
        print(0,end=" ")
        return
    sum=0
    for i in range(1,(int(sqrt(n))+1)):
        if n%i==0:
            if i==n//i:
                sum+=i
            else:
                sum+=i
                sum+=n//i
    n=sum-n
    print(n,end=" ")
    return proper(n)
n=10
print(n,end=" ")
proper(n)
