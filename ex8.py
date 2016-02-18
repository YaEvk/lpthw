#initialize a variable with the four %r
formatter = "%r %r %r %r"

#print output by different datas to variable formatter

#They are numbers
print formatter % (1, 2, 3, 4)
#They are characters
print formatter % ("one", "two", "three", "four")
#They are bool algebras
print formatter % (True, False, False, True)
#They are variables which defined at the first
print formatter % (formatter, formatter, formatter, formatter)
#They are strings
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#AND THIS PROGRAM, IS MY FIRST PROGRAM WITH COMMENTS.
