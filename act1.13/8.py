string=input("Enter a String : ")
a=len(string)
i=0
cc=0
lc=0
nc=0
while i<a:
    if string[i].isupper():
        cc+=1
    if string[i].islower():
        lc+=1
    if string[i].isdigit():
        nc+=1
    i+=1
print("Upper Case             :", cc)
print("Lower Case             :", lc)
print("Numeric Digits         :", nc)