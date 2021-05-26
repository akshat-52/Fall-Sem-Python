a=input("Enter a string: ")
if len(a)<7:
    print("String size is not sufficient!!!")
else:
    b=a[0:7]+a[-2]+a[-1]
    print(b)
