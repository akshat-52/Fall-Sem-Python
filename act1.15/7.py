
n=int(input("Enter number of rows needed: "))
a=65
i=1
while i<=n:
    j=1
    while j<=i:
        print(chr(a),end=' ')
        j+=1
        a+=1
    i+=1
    print(" ")
