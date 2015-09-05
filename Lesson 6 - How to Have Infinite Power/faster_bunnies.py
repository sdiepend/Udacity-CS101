#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

#My first solution
def fibonacci(n):
	i = 2
	j = 0
	k = 1
	if n == 0 or n == 1:
		return n
	while i <= n:
		print k
		t = k
		k = j + k
		j = t
		i = i + 1
	return k

# print fibonacci(0)
# print fibonacci(1)
# #print fibonacci(2)

# print fibonacci(50)
#>>> 14930352

# Udacity solution
def fibonacci2(n):
	current = 0
	after = 1
	for i in range(0, n):
		current, after = after, current + after
	return current

print fibonacci2(0)
print fibonacci2(1)
print fibonacci2(2)
print fibonacci2(47)