#swapping of 2 numbers without using 3rd variable
a=int(input("enter a:"))
b=int(input("enter b:"))
a,b=b,a
print(a)
print(b)



##enter a:5
##enter b:6
##6
##5


#another method for swapping of 2 numbers
a=int(input("enter a:"))
b=int(input("enter b:"))
a=a+b
b=a-b
a=a-b
print(a)
print(b)


##enter a:5
##enter b:6
##6
##5
