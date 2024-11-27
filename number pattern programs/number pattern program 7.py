n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(dummy,end=' ')
    print()
    dummy+=1
