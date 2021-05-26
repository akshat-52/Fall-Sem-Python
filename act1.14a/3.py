a=int(input("Enter number of rows: "))
b=0
for i in range(0, a+1):
    for j in range(i):
        print(b, end=" ")
    print("\n")
    b+=1