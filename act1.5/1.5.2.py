#storing BP, HRA, DA, MA
bp=input("Enter Basic Pay: ")
BasicPay=float(bp)

hra=0.15*float(bp)
da=0.25*float(bp) 
ma=0.15*float(bp)

Totalsal=float(hra)+float(da)+float(ma)+float(bp)
print("Total salary is:",Totalsal,"\n")
print("BP is:",bp,"\n")
print("HRA is:",hra,"\n")
print("DA is:",da,"\n")
print("MA is:",ma,"\n")