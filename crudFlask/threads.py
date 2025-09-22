import threading
import time

def print_number():
    for i in range(5):
        print("Number: ",i)
        time.sleep(1)

def print_letters():
    for ch in ["A","B","C","D","E"]:
        print("Letter:", ch)
        time.sleep(1)

t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both Threads finished")