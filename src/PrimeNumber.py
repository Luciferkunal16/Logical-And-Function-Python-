def is_prime(num):
    flag = True
    for i in range(2, num):
        if (num % i == 0):
            flag = False
            break
        else:
            flag = True
    if (flag == False):
        print("is not a prime number ")
    else:
        print("is a Prime Number")


if __name__ == "__main__":
    number = int(input("Enter a Number"))
    is_prime(number)
