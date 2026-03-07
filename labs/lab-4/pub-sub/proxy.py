import zmq

context = zmq.Context()

# Publishers connect here (XSUB), subscribers connect on XPUB.
xsub = context.socket(zmq.XSUB)
xsub.bind("tcp://*:5555")

xpub = context.socket(zmq.XPUB)
xpub.bind("tcp://*:5556")

zmq.proxy(xsub, xpub)

xsub.close()
xpub.close()
context.close()
