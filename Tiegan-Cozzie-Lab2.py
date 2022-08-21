# Bringing python modules into program
import math
import random

# Getting random int() and assigning it to a
a=random.randint(1,10)

# Getting a random floating point number between 0 and 20; assigning it to b
b=random.uniform(0,20)
b=round(b,2)

# Printing in terminal
print("a is "+ str(a))
print("b is "+ str(b))

# Making sure c is a float and is negative
c=float(input("Enter C: "))
c=-math.fabs(c)
print("c is "+ str(c))

# Printing unsolved equation
print(str(a)+ "x^2 +" +str(b)+"x" + str(c))

# solving equation
x1=(-b + math.sqrt(b**2-4*a*c))/(2*a)
x2=(-b - math.sqrt(b**2-4*a*c))/(2*a)

# Printing results
print("X= ",x1,"and",x2)
