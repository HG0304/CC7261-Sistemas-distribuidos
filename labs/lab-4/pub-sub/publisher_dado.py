from random import randint
from time import sleep
import zmq

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

while True:
    value = randint(1, 6)
    message = f"dado {value}"
    print(f"[P2] {message}", flush=True)
    pub.send_string(message)
    sleep(1)

pub.close()
context.close()
