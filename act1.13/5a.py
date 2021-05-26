a=int(input("Enter number of rows : "))
b=65
l=0
while l <= (a-1):
    j=0
    while j <= l:
        print(chr(b),end=' ')
        j+=1
    print(" ")
    l+=1
    b+=1