#python program to print all Disarium numbers between given range
print("\n<<< Hey Programmers !!! Welcome to python programming >>>")
print("<<< This code is for Printing Disarium numbers between the range as per user choice !!! >>>")
start=int(input("<<< Enter the Starting Number >>> : "))
ending=int(input("<<< Enter the Ending Number >>> : "))
for a in range(start, ending+1):
    string=str(a)
    check=a
    list=[]
    for i in string:
        i=int(i)
        list.append(i)
    m=0
    n=1
    for j in list:
        m+=j**n
        n+=1
    if m==check:
        print(a, end=" ")
print("\n<<< Thank You for using my Program !!! >>>")