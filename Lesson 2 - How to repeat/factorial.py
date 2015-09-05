# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
	i = 0
	num = 1
	while i < n:
		num = num * (n - i)
		i = i+1

	return num 

def factorial2(n):
	result = 1
	while n >= 1:
		result = result * n
		n = n -1
	return result



print factorial(0)
print factorial2(0)

print factorial(1)
print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
print factorial2(6)
#>>> 720

print factorial(52)