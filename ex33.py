i = 0
#initialize a void list
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 1
    print "Numbers Now: ", numbers
    print "At the bottom i is %d" % i

#when loop end, execute the code under here.
print "The numbers: "

#the "num" in here is just a formal argument
for i in numbers:
    print i
