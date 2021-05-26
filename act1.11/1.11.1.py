range1=int(input("Enter the range 1: "))

range2=int(input("Enter the range 2: "))

odd=0
even=0
for n in range(range1,range2):
    if n%2==0:
        even+=1
    else :
        odd+=1
print("No of even nos. are= ",even)
print("No of odd nos. are= ",odd)