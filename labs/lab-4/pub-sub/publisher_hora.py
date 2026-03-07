from datetime import datetime
from time import sleep
import zmq

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

while True:
    now = datetime.now().strftime("%H:%M:%S")
    message = f"hora {now}"
    print(f"[P1] {message}", flush=True)
    pub.send_string(message)
    sleep(1)

pub.close()
context.close()
