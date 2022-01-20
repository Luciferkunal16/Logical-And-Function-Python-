def reverse_of_number(num):
    reversed_number = 0
    while(num!=0):

        remainder=num%10
        reversed_number=reversed_number*10+remainder
        num//=10
    return reversed_number
if __name__=="__main__":
   print(reverse_of_number(int(input("Enter a Number to get its reverse number"))))
