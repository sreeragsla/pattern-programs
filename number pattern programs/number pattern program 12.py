n=int(input())
stars=n
dummy=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(dummy,end=' ')
    print()
    stars-=1
    dummy+=1
