#So what is the function of the little project?
#you must appoint two files title to be the argument of argv
#print what file you want to copy

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we should do these two on one line too, how?
input = open(from_file)
indata = input.read()

#len(), count a file's length.
print "The input file is %d bytes long." % len(indata)

#exist or not judge.
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#so you can open a file and execute the write order.
output = open(to_file, 'w')
#linked to the "indata" which read() the from_file.
output.write(indata)

print "Alright, all done."

output.close()
input.close()

#after that, you can use the cat command to look up your files(Linux limitted)
