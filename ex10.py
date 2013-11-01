tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
kuku =  "I am 6'2\" tall."  # escape double-quote inside string
anita = 'I am 6\'2" tall.' # escape single - quote inside string
kukunda = "I'm %s years old but you know gals it's that \\ 2" % 16
kinyatta = "I'm %r years old but you know gals it's that \\ 2" % 16


fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print kuku
print anita
print kukunda
print kinyatta