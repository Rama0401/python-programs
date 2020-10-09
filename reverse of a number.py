#reverse of a number
n=int(input("enter number:"))
while True:
    r=n%10
    n=n//10
    print(r,end="")
    if n==0:
        break



##o/p
##enter number:1234
##4321



#2nd method for reverse of a number
n=int(input("enter number:"))
res=0
while n:
    r=n%10
    n=n//10
    res=res*10+r
print(res)

##o/p
##enter number:1234
##4321
