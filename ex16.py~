#from sys import argv
from sys import argv

#set up argv
script, filename = argv

#call argv from keyboard
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN."

#prompt raw_input
raw_input("?")

#open the file that choosed by user
print "Opening the file..."
target = open(filename, 'w')

#clean a file by truncate
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#prompt raw_input to input your lines
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

#write lines to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#close file
print "And finally, we close it."
target.close()
