#python program to check Disarium number
print("<<< Hey Programmers !!! Welcome to python programming >>>")
print("<<< This code is for Checking whether the inputed number is Disarium or not !!! >>>")
element=input("Enter a Number to check it is Disarium or not : ")
check=int(element)
list=[]
for i in element:
    i=int(i)
    list.append(i)
d=0
c=1
for j in list:
    d+=j**c
    c+=1
if d==check:
    print("<<< This is a Disarium Number >>>")
else:
    print("<<< This is not a Disarium Number >>>")
print("\n<<< Thank You for using my Program !!! >>>")
