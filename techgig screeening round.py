n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    p=l[0]
    k=l[1]
    d=l[2]
    for i in range(d-1):
        mul=(d-1)*k
        res=mul+p
        print(res)
        break
        if d==2:
            mul=(d-1)*k
            res=mul+p
            print(res)
            break
        
