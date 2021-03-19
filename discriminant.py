import math

A = float(input("A:   "))
B = float(input("B:   "))
C = float(input("C:   "))
print("-----------------------------------------")

D = ( (B*B) - (4*A*C) )
print("The discriminative is", D)
print("-----------------------------------------")

if (D > 0):
    S1 = round( (-B + math.sqrt(D)) / (2 * A), 2 )
    S2 = round( (-B - math.sqrt(D)) / (2 * A), 2 )
    print(S1)
    print(S2)
elif (D == 0):
    S = round( (-B)/(2 * A), 2)
    print(S)
else:
    print("no solutions")
print("-----------------------------------------")