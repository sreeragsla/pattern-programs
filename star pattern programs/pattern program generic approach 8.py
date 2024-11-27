n=int(input())
stars=1
space=n//2
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        stars+=2
        space-=1
    else:
        stars-=2
        space+=1
