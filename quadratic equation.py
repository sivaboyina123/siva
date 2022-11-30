import cmath

print("General form:- ax**2 + bx + c")

a = int(input("Enter a(a!=0):"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

d = (b**2)-(4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)

sol2 = (-b+cmath.sqrt(d))/(2*a)

#print("\n")
print("Results for equation, {a}x**2+{b}x+{c}=0, are:")

if d>0:
    print("Type of roots: Two distinct real roots")

elif d==0:
    print("Type of Roots: Two equal real roots")

elif d<0:
    print("Type of root: Two complex roots")

print("solutions are{sol1} and {sol2}")
