
print 'Hello'
print "Hello"
hello = "Howdy"
print hello

name = "Stijn"
print "Hello " + name + "!" + "!"

# print "My name is" + 9

print "!" * 12
print "Hello " + name + "!" * 38

print name[0]
print name[-2]
print name[-1]

word = "assume"
print word[3]
print word[3:4]
print word[4:6]
print word[4:]
print word[:4]
print word[:]

# Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.

s = 'audacity'
print s[1].upper() + s[2:]
print s[:3] + s[3:]

t = "hi"

# For any string,
# s = '<any string>'
# which of the following always ha the value 0?

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print danton.find('audace')
print danton[danton.find('audace', danton.find('audace') + 1):]

# For any variables s and t that are strings, and i that is a number
# s = '<any string>'
# t = '<any string>'
# i = '<any number>'
s = 'udacity'
t = 'city'
i = 3
# which of these are equivalent to s.find(t,i):
print (s[i:].find(t) == s.find(t,i))
# s.find(t)[:i]
# s[i:].find(t) +i
# s[i:].find(t[i:])
# V None of these
