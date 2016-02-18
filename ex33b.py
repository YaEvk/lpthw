i = 0
numbers = []
def arbitrary_list(max_num, step):
    global i
    while i < max_num:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + step
        print "Numbers Now: ", numbers
        print "At the bottom i is %d" % i
    print "The numbers: "
    for number in numbers:
        print number
        
arbitrary_list(20, 10)
