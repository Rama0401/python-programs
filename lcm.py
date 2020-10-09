#lcm of 2 numbers
a=int(input("enter number:"))
b=int(input("enter number:"))
r=2
res=1
lcm=1
while True:
    if (a%r==0 and b%r==0):
        a=a//r
        b=b//r
        res=res*r
    else:
        r+=1
    if (a<r or b<r):
        break
lcm=res*a*b
print(lcm)

##o/p
##enter number:12
##enter number:24
##24
