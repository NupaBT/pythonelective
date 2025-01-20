a=int(input("enter a number "))
z=1
if a < 0:
     print("no square root for negative numbers.")
else:
    for num in range(a):
        if a==(z*z):
            break
        z=z+1
    z= (z+a/z)/2
    err=abs(a-z**2)
    if err==0:
        print("The Square root of ",a ,"is",z)
