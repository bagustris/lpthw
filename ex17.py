# ex17.py read more files, copy one files to another
# usage : python ex17.py fromfile tofile

from sys import argv
from os.path import exists

script, from_file, to_file=argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too. How?

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit return to continue, Ctrl-C to abort."
raw_input()

out_file = open(to_file, 'w')   #
out_file.write(indata)

print "Alright, all done"

out_file.close()
in_file.close()
