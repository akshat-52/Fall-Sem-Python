r=int(input("Enter number of rows: "))
n=0
k=1
for i in range(0, r+1):
    b=64
    if k % 2 != 0:
        for c in range(0,i):
            b+=1
            print(chr(b), end="\t")
    if k % 2 ==0:
        for d in range(0,i):
            b+=1
            print(chr(b), end="\t")
    k+=1
    print(end="\n")