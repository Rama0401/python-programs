#prime numbers btw range of n to m
n=int(input("enter number:"))
m=int(input("enter number:"))
for i in range(n,m+1):
    fc=0
    for j in range(1,i+1):
        if i%j==0:
            fc+=1
    if fc==2:
        print(i)

        
##enter number:1
##enter number:100
##2
##3
##5
##7
##11
##13
##17
##19
##23
##29
##31
##37
##41
##43
##47
##53
##59
##61
##67
##71
##73
##79
##83
##89
##97
