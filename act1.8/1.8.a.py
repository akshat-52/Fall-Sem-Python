i = 1
while i <= 7:
    j = 1
    print ("\n")
    while j <= i:
        if i%2 == 0:
            print ("#", end="\t")
        else:
            print("*", end="\t")
        j = j+1
    i = i+1