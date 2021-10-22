from math import *

u_1 = float(input("mean_1 "))
u_2 = float(input("mean_2 "))
v_1 = float(input("variance_1 ( σ1^2 ) "))
v_2 = float(input("variance_2(squared term) ( σ1^2 ) "))
r = float(input("correlation "))

variable = input("Condition on which variable ")
c = float(input("Condition "))

if variable == "2":
    print(
        f"New mean is {u_1 + (r * sqrt(v_1) * (c - u_2)) / sqrt(v_2)} and New standard deviation is {sqrt((1 - pow(r, 2)) * v_1)} ")

else:
    print(
        f"New mean is {u_2 + (r * sqrt(v_2) * (c - u_1)) / sqrt(v_1)} and New standard deviation is {(sqrt((1 - pow(r, 2)) * v_2))} ")

exit(0)        