import math

def findroots(a,b,c):
    discriminant=((b*b)-(4*a*c))
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1,root2
a=float(input("Enter the value for a:"))
b=float(input("Enter the value for b:"))
c=float(input("Enter the value for c:"))
root1,root2=findroots(a,b,c)
print(f"{root1},{root2}")