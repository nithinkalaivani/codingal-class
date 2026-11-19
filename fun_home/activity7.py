q2 = float(input("Enter a number: "))
q1 = float(input("Enter a number: "))

print("q1*q2=", q1*q2)
print("q1**2=", q1**2)
print("q2**2=", q2**2)
print("square root of q1=", q1**0.5)
print("square root of q2=", q2**0.5)
print("q1-q2=", q1-q2)
print("q2-q1=", q2-q1)
print("q1+q2=", q1+q2)

if q1>q2:
    print("q1 is greater than q2")
elif q1<q2:
    print("q2 is greater than q1")
else:
    print("q1 and q2 are equal")
