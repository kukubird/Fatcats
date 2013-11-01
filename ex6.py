x = "There are  %d types of people." % 10         #decalring x and assinging the format operator to 10.
binary = "binary"              # assinging variable binary to string binary
do_not = "don't"                # assinging variable don_not to string don't
y = "Those who know %s and those who %s." % ( binary , do_not)    # 3.a string is put inside a string 

print x
print y

print "I said:  %r." %x #prints sentence with quotes ( 1.a string is put inside a string)
print "I also said:  '%s'." %y # doesn't print the sentence with quotes (2.a string is put inside a string)
# unless quotes are put around '%s'.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of...."
e = " a string with a right side."

print w + e
