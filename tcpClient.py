# client.py  
import socket
import time
import subprocess
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# change to the server ip address

host = socket.gethostname() 
#host = "0:0:0:0:0:0:0:1"                          
print host
port = 9998


currTime = time.time()
# connection to hostname on the port.
s.connect((host, port))                               
# Receive no more than 1024 bytes
tm = s.recv(1024)                                     
afterTime = time.time()

elapsedTime = afterTime - currTime
timeAdjusted = elapsedTime / 2
print( " That took " + str(elapsedTime) + " secs")


servertime = float(tm.decode('ascii'))

finalTime = servertime + timeAdjusted 

print(" Ajusted new time for RTT " + str(finalTime))
subprocess.call("sudo gdate -s '@" + str(finalTime) +"'" , shell=True)
print("DONE")
# received time
s.close()