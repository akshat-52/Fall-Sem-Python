rows=int(input("Enter number of rows required: "))

a = 65
for i in range(0,rows):
    for j in range(0,i+1):
        print(chr(a),end=' ')
        a +=1
    print("")

