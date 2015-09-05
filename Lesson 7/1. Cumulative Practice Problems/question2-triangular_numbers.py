# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive 
# integer n and returns the nth triangular number.

# My solution
def triangular(n):
	i = 1
	sum = 0
	while i <= n:
		sum = sum + i
		i = i + 1
	return sum

# Udacity solution
def triangular2(n):
	number = 0
	for i in range(1,n+1):
		number = number + i
	return number


print triangular(1)
print triangular2(1)
#>>>1

print triangular(3)
print triangular2(3)
#>>> 6

print triangular(10)
print triangular2(10)
#>>> 55
