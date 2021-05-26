number=int(input("Enter the number to find factorial: "))
i=number
factorial=1
print("factorial of",number,"is")
while i > 1:
    factorial=factorial*i
    print(i,end=' X ')
    i-=1
print("1 = ",factorial)