#even count and odd count in a number
n=int(input("enter number:"))
even_count=0
odd_count=0
while n:
    r=n%10
    n=n//10
    if r%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count,odd_count)


##o/p
##enter number:12345
##2 3
