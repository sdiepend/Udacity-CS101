# Deep Count 

# The built-in len operator outputs the number of top-level elements in a List,
# but not the total number of elements. For this question, your goal is to count
# the total number of elements in a list, including all of the inner lists.

# Define a procedure, deep_count, that takes as input a list, and outputs the
# total number of elements in the list, including all elements in lists that it
# contains.


# For this procedure, you will need a way to test if a value is a list. We have
# provided a procedure, is_list(p) that does this:

def is_list(p):
    return isinstance(p, list)

# It is not necessary to understand how is_list works. It returns True if the
# input is a List, and returns False otherwise.



# My solution, it worked on the test cases of the video, but actually it's not 
# correct. If you test it for the edge case where p = [] it will return "1" which 
# is incorrect because it's an empty list. Also it's not very "clean".
def deep_count(p):
	if is_list(p) == False:
		return 1
	elif len(p) == 0:
		return 1
	else:
		total = 0
		for e in p:
		    total = total + deep_count(e)
		    if is_list(e) == True and len(e) != 0:
		    	total = total + 1
		return total

# Solution from Udacity video
def deep_count2(p):
	sum = 0
	for e in p:
		sum = sum + 1
		if is_list(e):
			sum = sum + deep_count2(e)
	return sum

print deep_count([])
print deep_count2([])

print deep_count([[]])
print deep_count2([[]])


print deep_count([1, 2, 3])
print deep_count2([1, 2, 3])
#>>> 3

# The empty list still counts as an element of the outer list
print deep_count([1, [], 3])
print deep_count2([1, [], 3])
#>>> 3 

print deep_count([1, [1, 2, [3, 4]]])
print deep_count2([1, [1, 2, [3, 4]]])
#>>> 7

print deep_count([[[[[[[[1, 2, 3]]]]]]]])
print deep_count2([[[[[[[[1, 2, 3]]]]]]]])
#>>> 10

 