import threading
from time import sleep
class Messaenger(threading.Thread):
    def run(self):
        for _ in range(10):
            sleep(1)
            print(threading.currentThread().getName())


x = Messaenger(name='Send out messages')
y = Messaenger(name='Get messages')
x.start()
y.start()
