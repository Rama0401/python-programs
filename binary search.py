##binary search
##array=[1,4,7,3,5,6,8,9,2]
##key=int(input())
##array.sort()
##i=0
##j=len(array)-1
##while i<=j:
##    m=(i+j)//2
##    if array[m]==key:
##        print("yes")
##        break
##    elif array[m]<key:
##        i=m+1
##    else:
##         j=m-1



##triplent sum
##array=[12,2,3,1,4,6,9]
##array.sort()
##s=25
##for i in range(len(array)-2):
##    for j in range(i+1,len(array)-1):
##        for k in range(j+1,len(array)):
##            if array[i]+array[j]+array[k]==s:
##                print(array[i],array[j],array[k])
##

    

##tripilent sum pr bernnes algorithm
##array=[12,2,3,1,4,6,9]
##array.sort()
##s=25
##for i in range(len(array)):
##    p=s-array[i]
##    j=i+1
##    k=len(array)-1
##    while j<k:
##        if array[j]+array[k]==p:
##            print(array[i],array[j],array[k])
##            break
##        elif array[j]+array[k]<s:
##            j+=1
##        else:
##            k-=1



















































