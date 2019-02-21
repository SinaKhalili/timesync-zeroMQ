import zmq
import time
import sys

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
while True:
    #current time = some time
    #here it should be sending the current time
    # print current time set current time
    topic = "currentTime"
    messagedata = time.time()
    print "%s %f" % (topic, messagedata)
    # send current time
    currentTime = time.time()
    socket.send("%s %f" % (topic, messagedata))
    time.sleep(1)
    


