Number = int(input(" Please Enter any Number: "))
num = 0
for i in range(2, (Number//2 + 1)):
    if(Number % i == 0):
        num += 1
        break
if (num == 0 and Number != 1):
    print("It is a Prime Number.")
else:
    print("It is not a Prime Number.")