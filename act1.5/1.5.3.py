cir_r = int(input("Enter the radius of circle : "))
rec_l = int(input("Enter the length of the rectangle : "))
rec_w = int(input("Enter the width of the rectangle : "))
area_cir = (cir_r*cir_r) * 22/7
area_rec = rec_l * rec_w
print("Area of the circle is = ",area_cir)
print("Area of the rectangle is = ",area_rec)
if area_cir > area_rec :
    print("Area of the circle is largest")
else :
    print("Area of the rectangle is largest")