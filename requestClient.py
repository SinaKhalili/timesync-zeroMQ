import zmq
import sys
import time
import subprocess

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
 

	#  Get the reply.



timeBefore = time.time()
socket.send ("TimeRequest")
TimeReplyMessage = socket.recv()
timeAfter = time.time()
elapsedTime = timeAfter - timeBefore
timeAdjusted = elapsedTime / 2
print( " That took " + str(elapsedTime) + " secs")

finalTime = float(TimeReplyMessage) + timeAdjusted 

print(" Ajusted new time for RTT " + str(finalTime))
subprocess.call("sudo gdate -s '@" + str(finalTime) +"'" , shell=True)
print("DONE")

#setTime = elapsedTime+ TimeReplyMessage
	#received set the time
print "Received reply [", TimeReplyMessage, "]"

# set the time






