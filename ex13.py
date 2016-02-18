#what is "sys"?
from sys import argv

script, charm, sexy = argv

#script is the argument of the script name.
print "The script is called", script
#raw_input to get your input
first = raw_input("what's your first variable?")
print "your first variable is: %r" % (first)
second = raw_input("what's your second variable?")
print "your second variable is: %r" % second
third = raw_input("what's your first variable?")
print "your third variable is: %r" % third

#They are arguments in argv, you should input them in initial.
print "Your life is:", charm
print "You look:", sexy
