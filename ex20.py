from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

#rewind->restart! by seek(locate the offset the front)
def rewind(f):
    f.seek(0)

#'f' is a format argument, which point to file
def print_a_line(line_count, f):
    print line_count, f.readline()
    
current_file = open(input_file)

print "First let's print the whole file:\n"

#the first print
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#turn to the front text
rewind(current_file)

#the second print with line number
print "Let's print three lines:"

#the mark of sequence number of the line
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)



