import random


def function_coupon_number():
    set1 = set()
    set1.add(random.randint(1000, 9999))


if __name__ == "__main__":
    number = int(input("Enter how many coupon number you want"))
    for i in range(1,number):
        function_coupon_number()
    for i in set1:
        print(i)
