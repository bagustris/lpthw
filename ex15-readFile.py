# ex15.py: writing 2 files
from sys import argv

script, filename=argv

txt=open(filename)  #using new command 'open' to open the file

print "Here's your file %r: " %filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
