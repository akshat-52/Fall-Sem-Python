a=int(input("Enter number of rows: "))
b=2
c=1
for i in range(1, a+1):
    for j in range(0, i+c):
        print(b, end='\t')
    print("\n")
    b+=2
    c+=1