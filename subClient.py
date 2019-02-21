import sys
import zmq
import time
import subprocess

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

    # Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print "collecting currentTime"
socket.connect ("tcp://localhost:%s" % port)
 
# Subscribe to zipcode, default is NYC, 10001
topic = "currentTime"
socket.setsockopt(zmq.SUBSCRIBE, topic)

# Process 5 updates
total_value = 0

timeBefore = time.time()
string = socket.recv()
timeAfter = time.time()
topic, recievedTime = string.split()
elapsedTime = timeAfter - timeBefore
finalTime = (elapsedTime / 2.0 )+ float(recievedTime)

print(" Ajusted new time for RTT " + str(finalTime))
subprocess.call("sudo gdate -s '@" + str(finalTime) +"'" , shell=True)
print("DONE")

#set the time

 
      