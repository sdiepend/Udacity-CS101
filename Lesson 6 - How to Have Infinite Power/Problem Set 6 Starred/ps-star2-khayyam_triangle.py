# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.

# Mysolution, It's a bit large, I think it can be a bit smaller with same changes (recursive)
def my_triangle(n):
	if n == 0:
		return []
	elif n == 1:
		return [[1]]
	elif n == 2:
	 	return [[1],[1,1]]
	else:
		rowbefore = my_triangle(n-1)[-1]
		# print rowbefore
		i = 1
		currentrow = [1] * n
		while i < len(rowbefore):
			# print rowbefore[i-1]
			# print rowbefore[i]
			currentrow[i] = rowbefore[i-1] + rowbefore[i]
			i = i + 1
		newrows = my_triangle(n-1) + [currentrow]
		# print newrows
		return newrows

# Mysolution cleaned (recursive)
def my_triangle2(n):
	if n == 0:
		return []
	elif n == 1:
		return [[1]]
	else:
		rowsbefore = my_triangle2(n-1)
		i = 1
		currentrow = [1] * n
		while i < len(rowsbefore[-1]):
			currentrow[i] = rowsbefore[-1][i-1] + rowsbefore[-1][i]
			i = i + 1
		return rowsbefore + [currentrow]

# Solution from Udacity video (iterative)
def u_triangle(n):
	result = []
	current = [1]
	for unused in range(0, n):
		result.append(current)
		current = make_next_row(current)
	return result

def make_next_row(row):
	result = []
	prev = 0
	for e in row:
		result.append(e + prev)
		prev = e
	result.append(prev)
	return result

#For example:

print my_triangle(0)
print my_triangle2(0)
print u_triangle(0)
#>>> []

print my_triangle(1)
print my_triangle2(1)
print u_triangle(1)
#>>> [[1]]

print my_triangle(2)
print my_triangle2(2)
print u_triangle(2)
#>> [[1], [1, 1]]

print my_triangle(3)
print my_triangle2(3)
print u_triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

print my_triangle(6)
print my_triangle2(6)
print u_triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
