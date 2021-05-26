string=input("Enter the String : ").capitalize()
temp = ""
i=0
a=len(string)
while i<a:
    if string[i]== " ":
        k = i+1
        temp = temp + " " + string[k].upper()
        i+=2
        continue
    else:
        temp=temp+string[i]
    i+=1
print("The String in Title Case is : ",temp)