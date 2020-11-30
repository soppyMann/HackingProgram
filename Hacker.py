import random
import time
import Watchlist

def hack(target):
    print("Hacking {target}...".format(target=target))
    for i in range(30):
        print("{rander}%".format(rander=random.randint(0, 99)))
        time.sleep(1)
    print("100%")
    time.sleep(3)
        
    Watchlist.Error()
