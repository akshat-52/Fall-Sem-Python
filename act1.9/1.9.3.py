num=int(input("Enter the number: "))
lim=int(input("Enter the limit: "))
a=num
print("the multiples of",num,"are")
while lim !=0:
    print(num,end=',')
    num=num+a
    lim=lim-1