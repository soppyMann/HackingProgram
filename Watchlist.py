import random
import time

def Error():
    watchlist = ["CIA", "FBI"]
    print("CRITICAL ERROR!!!")
    time.sleep(1.5)
    print("YOUR IP ADDRESS HAS BEEN LEAKED!!!")
    time.sleep(1.5)
    print("YOU HAVE BEEN ADDED TO THE {watchlist} WATCHLIST!!!".format(watchlist = random.choice(watchlist)))
    time.sleep(1)
    print("BE CAREFUL!!!")
