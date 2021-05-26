ch=input("DO YOU WANT TO ENCODE (YES/NO): ").lower()
if ch == "yes" :
    original_string=input("ENTER THE STRING TO BE ENCODED :")
    en_a=original_string.replace('a', '5')
    en_b=en_a.replace('b', '+')
    en_c=en_b.replace('c', '$')
    print("THE ORIGINAL STRING : ",original_string)
    print("THE ENCODED STRING : ", en_c)
elif ch == "no":
    print("OKAY HAVE A GREAT TIME")
