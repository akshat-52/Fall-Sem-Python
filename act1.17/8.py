#python program to check Pronic number
print("\n<<< Hey Programmers !!! Welcome to python programming >>>")
print("<<< This code is for Checking whether the input is Pronic Number or not !!! >>>")
element=int(input("<<< Enter a Number to check it is Pronic or not >>> : "))
if element!=0:
    for i in range(0,element+1):
        if i*(i+1)==element:
            print("<<< It is a Pronic Number >>>")
            break
    else:
        print("<<< It is not a Pronic Number >>>")
else:
    print("<<< It is not a Pronic Number >>>")
print("\n<<< Thank You for using my Program !!! >>>")