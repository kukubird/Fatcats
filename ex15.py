from sys import argv
filename = "ex15_sample.txt"

txt = open("ex15_sample.txt")

print"Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()