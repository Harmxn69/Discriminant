import math

A = float(input("A:   "))
B = float(input("B:   "))
C = float(input("C:   "))

D = ( (B*B) - (4*A*C) )
print("\nThe discriminative is", D)

if (D > 0):
    S1 = round( (-B + math.sqrt(D)) / (2 * A), 2 )
    S2 = round( (-B - math.sqrt(D)) / (2 * A), 2 )
    print("Answer 1: ",S1)
    print("Answer 2: ",S2)
elif (D == 0):
    S = round( (-B)/(2 * A), 2)
    print(S)
else:
    print("\nno solutions")
print("-------------------------------------")