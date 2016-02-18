x= "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y="Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r ." % x
print "I also said %r." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#The %r here I don't know it means.

print joke_evaluation % hilarious

#I got it! Combine the two sentences, we will find that thing!
#"Isn't that joke so funny?! %r" % False

#So it's nothing that you dipart the two variables in two sentences.

w = "This is the left side of..."
e = "a string with right side."

print w + e
