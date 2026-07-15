#print("hello everybody")


from math import sqrt
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))
print(f"The roots are {(-b + sqrt(b*b-4*a*c))/(2*a)} and {(-b - sqrt(b*b-4*a*c))/(2*a)}")