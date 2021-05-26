a=int(input("Enter the number of rows needed : "))
b=65
c=1
d=1
while c<=a:
    j=1
    while j<=c:
        if c%2!=0:
            print(chr(b), end=" ")
        else:
            print(d, end=" ")
        j+=1
    d+=1
    print(" ")
    c+=1
    b+=1