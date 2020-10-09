#gcd of 2 numbers
a=int(input("enter number:"))
b=int(input("enter number:"))
if a>b:
    for i in range(b,1,-1):
        if a%i==0 and b%i==0:
            print(i)
            break
else:
    for i in range(b,1,-1):
        if a%i==0 and b%i==0:
            print(i)
            break


##o/p
##enter number:36
##enter number:44
##4
