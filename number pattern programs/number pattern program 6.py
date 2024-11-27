n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
        if row%2==0:
            dummy-=1
        else:
            dummy+=1
    print()
