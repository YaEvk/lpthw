ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
print stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # stack rule
    print "Adding: ", next_one
    stuff.append(next_one) # append word to stuff
    print "there's %d items now." % len(stuff) # show length of stuff, and contrast it to loop-condition

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
# you can look for the rule of digit number of python in the EU python book.
print stuff.pop() # stack rule
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stealler!
