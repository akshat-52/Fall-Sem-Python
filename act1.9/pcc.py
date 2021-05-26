num=int(input("Enter the number for finding the factorial: "))
factorial=1
if num<0:
    print("Sorry factorial does not exist! try positive number")
elif num==0:
    print("The fatorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The fatorial of",num,"is",factorial)

