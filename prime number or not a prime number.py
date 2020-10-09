
#prime number or not a prime number
n=int(input("enter number:"))
factor_count=0
for i in range(1,n+1):
    if n%i==0:
        factor_count+=1
if factor_count==2:
    print("prime number")
else:
    print("not a prime number")

##o/p
##enter number:7
##prime number
