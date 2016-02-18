print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# Write poem as a string note """
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

# Some arithmetic
five = 10 - 2 + 3 - 6

# Broke the program and then fixed it
# print "This should
# be five: %s" % five
print "This should be five: %s" % five

# definition of secret formula
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# Assign value for startpoint and do secret_formula
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

start_point = start_point / 10

# We can put function as a parameter
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates" % secret_formula(start_point)
