# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(p, ele):
	if ele in p:
		return p.index(ele)
	else:
		return -1

def find_element(p, ele):
	if ele not in p:
		return -1
	return p.index(ele)



print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1