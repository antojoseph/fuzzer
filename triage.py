import sys
import subprocess
import re
import time
from os import listdir
if sys.argv[1] == '-h':
    print 'Usage:\n '
    print 'get_uniquecrash.py <log_file>'
    sys.exit()

log_file = sys.argv[1]
new_crashes = {}

offset_line_to_file = 2
f = open(sys.argv[1], "r")
lines = f.readlines()

#parse every line of the current log
print "Total Number  of lines" +str(len(lines))
for x in range(0, len(lines)):
        
        strings = ("SIGSEGV", "SIGSEGV", "SIGFPE","SIGILL")
        if any(s in lines[x] for s in strings):
          if "F/libc" in lines[x]:
            print "crash file :"+lines[x - offset_line_to_file]
            print lines[x] 

