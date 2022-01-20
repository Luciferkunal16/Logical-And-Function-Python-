if __name__=="__main__":
   def funtion_is_leap_year(year):
       if (year > 999 and year < 10000):
           if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
               print("{} is a leap year".format(year))
           else:
               print("{} is not a leap year".format(year))
       else:
           print("Invalid leap year")
year=int(input("Enter The Year (should be 4 digit number)"))
funtion_is_leap_year(year)