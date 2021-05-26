n=int(input("Enter the number of your choice: "))
if n==1:
    print("1 is Neither prime nor composite.")
elif (n==2 or n==3):
    print("It is a prime number.")
elif (n%2==0 or n%3==0):
    print("It is a composite No.")
else:
    print("It is a prime number.")