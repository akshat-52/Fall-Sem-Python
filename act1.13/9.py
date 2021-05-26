string=input("Enter the String : ")
check=input("Enter the string to be searched : ")
a=len(string)
b=len(check)
c=0
for j in range(a):
    if string[j:j+b]==check:
        c+=1
print("The number of occurence of", check, "is : ", c)