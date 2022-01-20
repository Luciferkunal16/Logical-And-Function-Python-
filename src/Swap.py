def function_swap(a,b):
    temp=a
    a=b
    b=temp
    print("a={} b={}".format(a, b))
if __name__ == "__main__":
    a = 10
    b = 20
    print("Number Before Swapping")
    print("a={} b={}".format(a, b))
    print("Number After Swapping")
    function_swap(a,b)

