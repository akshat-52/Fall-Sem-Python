d1,d2=0,1
limit = 2
n_terms = int(input("Enter number of terms: "))
if n_terms <= 0:
    print("Invalid input !!")
elif n_terms == 1:
    print(d1)
else:
    print('0,1',end=',')
    while limit < n_terms:
        cal=d1+d2
        d1=d2
        d2=cal
        limit+=1
        print(cal,end=',')