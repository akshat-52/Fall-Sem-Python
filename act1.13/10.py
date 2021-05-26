var=input("Enter the String :")
i=0
a=0
b=0
while i<len(var):
    if ord(var[i])>=65 and ord(var[i])<=90:
        a+=1
    elif ord(var[i])>=97 and ord(var[i])<=122:
        a+=1
    elif ord(var[i])>=48 and ord(var[i])<=57:
        a+=1    
    else:
        b+=1
    i+=1
print("Total number of characters except numeric digits (0-9) and alphabets (both a-z and A-Z):", b)