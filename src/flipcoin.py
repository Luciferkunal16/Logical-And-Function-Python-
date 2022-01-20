import random
import time

if __name__=="__main__":
    random_number=random.randint(0,1)
    print("Coin is Tossing....")
    time.sleep(1);
    if(random_number==0):
        print("Head")
    else:
        print("Tail")