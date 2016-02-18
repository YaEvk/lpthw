#import a module in sys.
from sys import argv

#appoint the argument to argv.
script, filename = argv

#The function open to a variable "txt".
txt = open(filename)

#cooperate with import argv, call argument back to print.
print "Here is your file %r:" % filename
#call function read, act on txt
print txt.read()
txt.close()

print "Type the filename again:"
#appoint the variable file_again to input.
file_again = raw_input("> ")
#appoint the variable txt_again, call open function to open file_again
txt_again = open(file_again)

#call function read, act pn txt_again.
print txt_again.read()
txt_again.close()
