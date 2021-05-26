a=int(input("Enter 1st angle: "))
b=int(input("Enter 2nd angle: "))
c=int(input("Enter 3rd angle: "))
if a+b+c<=180:
    a1=a
    a2=b
    a3=c
    h=90
    if a1==h or a2==h or  a3==h:
        print("It is a right angled triangle")
    elif a1<h and a2<h and a3<h:
        print("It is acute angled triangle")
    else:
        print("It is an obtuse angled traingle")
else:
    print("It is not a triangle")