import math

if __name__=="__main__":
    def power_of_two(number):
        for i in range(1,number):
            print(math.pow(2,i))

number=int(input("Enter a Number"))
if (number>0 and number<31):
    power_of_two(number)
else:
    print("Wrong chooice")