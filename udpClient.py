import socket
import subprocess
import time

msgFromClient       = "Send Time"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket



 
currTime = time.time()
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
afterTime = time.time()

elapsedTime = afterTime - currTime
timeAdjusted = elapsedTime / 2
print( " That took " + str(elapsedTime) + " secs")

finalTime = float(msgFromServer[0]) + timeAdjusted 

print(" Ajusted new time for RTT " + str(finalTime))
subprocess.call("sudo gdate -s '@" + str(finalTime) +"'" , shell=True)
print("DONE")
