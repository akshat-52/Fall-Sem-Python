#python code to count the number of vowels in the string
vowels=['a','e','i','o','u']
string=input("Enter a string : ").lower()
l=len(string)-1
i=0
v_count=0
while i<=l:
    if string[i] in vowels:
        v_count+=1
    i+=1
print("The number of vowels in the given string is : ",v_count)