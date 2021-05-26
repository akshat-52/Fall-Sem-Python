a=int(input("Enter number of rows: "))
b=65
d=1
lin=1
for i in range(1, a+1):
    for j in range(0,i):
        if lin%2!=0:
            print(chr(b), end='\t')
        else:
            print(d, end='\t')
    d+=1
    lin += 1
    b += 1
    print("\n")