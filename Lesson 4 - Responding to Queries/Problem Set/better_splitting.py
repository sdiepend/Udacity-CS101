# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

# My first solution
def split_string(source,splitlist):
	i = 0
	lastm = -1
	result = []
	for c in source:
		for d in splitlist:
			if c == d:
				substr = source[lastm+1:i]
				if substr != '':
				    result.append(substr)
				lastm = i
		i = i + 1
	substr = source[lastm+1:len(source)]
	if substr != '':
	    result.append(substr)
	return result

# Udacity solution
def split_string_udacity(source,splitlist):
	output = []
	atsplit = True #At a split point
	for char in source: #iterate through string by each letter
	    if char in splitlist:
	    	atsplit = True
	    else:
	    	if atsplit:
	    		output.append(char)
	    		atsplit = False
	    	else:
	    		#add character to last word
	    		output[-1] = output[-1] + char
	return output



out = split_string("This is a test-of the,string separation-code!"," ,!-")
out_udacity = split_string_udacity("This is a test-of the,string separation-code!"," ,!-")
print out
print out_udacity
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
out_udacity = split_string_udacity("After  the flood   ...  all the colors came out.", " .")
print out
print(out_udacity)
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
out_udacity = split_string_udacity("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
print(out_udacity)
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']