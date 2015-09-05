# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(p, ele):
	pos = -1
	i = -1
	for e in p:
		i = i + 1
		if e == ele:
			pos = i
			break
	return pos

def find_element2(p, ele):
	i = 0
	for e in p:
		if e == ele:
			return i
		i = i + 1
	return -1



print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1