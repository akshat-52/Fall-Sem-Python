#python code to check whether the entered string is palindrome or not
string=input("Enter a string : ").lower()
a=string[::-1]
if a==string:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")
    print("PROOF !")
    print("The given string is : ",string)
    print("Its reverse is : ",a)