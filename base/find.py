import random

x = random.randint(0, 20)
print("\n------Find a number in 0-20------\n")
for i in range(0, 3):
    a = input("input the number:")
    if int(a) < x:
        print("small")
    elif int(a) > x:
        print("big")
    else:
        print("Right")
        print(" 1 yuan")
        break
print("\nThe number is %s" % x)
