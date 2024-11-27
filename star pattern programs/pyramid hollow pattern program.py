n=int(input())
stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        if row==1 or row==n:
            print('*',end=' ')
            print(' ',end=' ')
        else:
            if st==1 or st==stars:
                print('*',end=' ')
                print(' ',end=' ')
            else:
                space=2
                for sp in range(1,space+1):
                    print(' ',end=' ')
                space+=1
    print()
    stars+=1
    spaces-=1

                    
