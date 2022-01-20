def fun_is_fabonacii(n):
    """

    :param n:
    :return:
    """
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


if __name__ == "__main__":
    num = int(input("Enter a number whose Fabonaci you want"))
    print(fun_is_fabonacii(num))
