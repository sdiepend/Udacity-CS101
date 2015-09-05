# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(num):
    i = 1
    while i <= num:
        print i
        i = i+1    

def print_numbers2(n):
    i = 0
    while i < n:
        i = i +1
        print i           
   



print_numbers(3)
print_numbers2(3)

print "zerotest"
print_numbers2(0)
#>>> 1
#>>> 2
#>>> 3