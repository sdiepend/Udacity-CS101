# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(x,y,z):
	if biggest(x,y,z) == x:
	    return bigger(y,z)
	if biggest(x,y,z) == y:
		return bigger(x,z)
	if biggest(x,y,z) == z:
		return bigger(x,y)





print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7

print(median(6,6,6))