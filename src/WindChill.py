def wind(t, v):
    w = (355.74 + 0.6215 * t + (.4275 * t - 35.75)) * pow(v, 0.16)  # calculation
    print(w)


if __name__ == "__main__":
    try:
        t = int(input("enter the temperature in Fahrenheit "))
        v = int(input("enter the speed in miles"))
        if t < 50 and 3 < v < 120:  # condition check
            wind(t, v)  # calls the  method
        else:
            print("enter the the value of t less than 50 and v more than 3 and less than 12")
    except ValueError:
        print("Input only accepts decimal numbers")
