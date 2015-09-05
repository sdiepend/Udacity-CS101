# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

# Method 1, very verbose, worst way to solve it
def biggest(a, b, c):
	if (a > b > c) or (a > b == c) or (a > c > b) or (a == b > c) or (a == c > b) or (a == b == c):
		return a
	if (b > a > c) or (b > a == c) or (b > c > a) or (b == a > c) or (b == c > a) or (a == b == c):
		return b
	if (c > a > b) or (c > a == b) or (c > b > a) or (c == a > b) or (c == b > a) or (a == b == c):
	    return c

# Method 2, verbose, better way to solve it
def biggest2(a, b, c):
	if a > b:
		if a > c:
			return a
		else:
			return c
	else:
		if b > c:
			return b
		else:
			return c

# Method 3, best way to s
def bigger(a, b):
	if a > b:
		return a
	else:
		return b

def biggest3(a,b,c):
	return bigger(bigger(a,b),c)

def biggest4(a,b,c):
	return max(a,b,c)


print "Test1"
print biggest(3, 6, 9)
print biggest2(3, 6, 9)
print biggest3(3, 6, 9)
print biggest4(3, 6, 9)
#>>> 9

print "Test2"
print biggest(6, 9, 3)
print biggest2(6, 9, 3)
print biggest3(6, 9, 3)
#>>> 9

print "Test3"
print biggest(9, 3, 6)
print biggest2(9, 3, 6)
print biggest3(9, 3, 6)
#>>> 9

print "Test4 met cijfers (3, 3, 9)"
print biggest(3, 3, 9)
print biggest2(3, 3, 9)
print biggest3(3, 3, 9)
#>>> 9

print "Test5"
print biggest(9, 3, 9)
print biggest2(9, 3, 9)
print biggest3(9, 3, 9)
#>>> 9

print "Test6"
print biggest(6,6,6)
print biggest2(6,6,6)
print biggest3(6,6,6)