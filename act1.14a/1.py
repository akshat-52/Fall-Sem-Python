r=int(input("Enter number of rows needed: "))
n=0
j=1
for i in range(0, r+1):
    if j % 2 != 0:
        for c in range(0,i):
            print('#', end=" ")
    if j % 2 == 0:
        for d in range(0,i):
            print('*', end=" ")
    j += 1
    print(end="\n")