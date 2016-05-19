import sys
import os

new_crashes = []
path_to_generated_samples = "/Users/anto/myfuzzer/fuzzer/generated_samples_folder/"
path_for_confirmed_samples ="/Users/anto/myfuzzer/fuzzer/crashes/"

#Move files to triage folder
def move_crashes_to_triage():
    try:
        for x in range(0,len(new_crashes)):
            print new_crashes[x]
            print path_to_generated_samples + new_crashes[x]
            print path_for_confirmed_samples + new_crashes[x]

            if  os.path.isfile(path_to_generated_samples+new_crashes[x]):
                os.rename(path_to_generated_samples+new_crashes[x], path_for_confirmed_samples+new_crashes[x])
    except Exception, e:
        print str(e)


if sys.argv[1] == '-h':
    print 'Usage:\n '
    print 'get_uniquecrash.py <log_file>'
    sys.exit()

log_file = sys.argv[1]





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
            #print "Filename:"+lines[x - offset_line_to_file][32:].strip()
            new_crashes.append(lines[x - offset_line_to_file][32:].strip())

move_crashes_to_triage()



            
            #run triage and process tombstone files
            #have a beer :)