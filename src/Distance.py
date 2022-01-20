import math

if __name__=="__main__":
    def func_Distance(x,y):
       return math.sqrt(math.pow(x,2)+math.pow(y,2))
x=int(input("Enter the Value of x "))
y=int(input("Enter the Value of Y "))
print(func_Distance(x,y))