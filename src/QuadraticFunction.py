def quadraticFunctions (a, b, c):
    print("Given quadratic equation is:", a, "x^2 +", b, "x + ", c)
    d = (b * b) - (4 * a * c)
    if d > 0:
        print("Roots are real and unequal")
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print("First Root ", root1)
        print("Second Root ", root2)

    elif d == 0:
        print("Roots are real and equal")
        root1 = (-b + math.sqrt(d)) / (2 * a)
        print("First Root ", root1)

    else:
        print("Root are imaginary")
if __name__=="__main__":
    try:
        a = int(input("Enter the value of a "))
        b = int(input("Enter the value of b "))
        c = int(input("Enter the value of c "))
        quadraticFunctions(a, b, c)
    except ValueError:
        print("Input only accepts decimal numbers")
