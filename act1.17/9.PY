b=1
for i in range(0,5):
    for j in range(5,0,-1):
        if j==b:
            print("*",end='')
            continue
        print(j,end='')
    print(end='\n')
    b+=1