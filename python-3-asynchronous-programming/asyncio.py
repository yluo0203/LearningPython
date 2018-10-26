# Udemy asyncio 
# Event loop task manager

import time
from datetime import datetime

# def foo():
#     for i in range(100000):
#         print(i)
#         yield
#         time.sleep(0.5)

# action = foo()

# Ctrl + C for stop.
# next(action)
# print("Is a break!")
# next(action)

def print_message_periodical(interval_seconds, message = 'keep alive.'):
    while True:
        print(f'{datetime.now()} - {message}')
        start = time.time()
        end = start + interval_seconds
        while True:
            now = time.time()
            if now >= end:
                break

if __name__ == "__main__":
    print_message_periodical(3, "Three")
    # print_message_periodical(10, "Ten")
