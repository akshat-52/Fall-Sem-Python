#python program to check Harshad number
print("\n<<< Hey Programmers !!! Welcome to python programming >>>")
print("<<< This code is for Checking whether the input is Harshad Number or not !!! >>>")
element=input("<<< Enter a Number to check it is Harshad or not >>> : ")
check=int(element)
sum=0
for i in element:
    i=int(i)
    sum+=i
if check % sum == 0:
    print("<<< It is a Harshad Number >>>")
else:
    print("<<< It is not a Harshad Number !!! >>>")
print("\n<<< Thank You for using my Program !!! >>>")