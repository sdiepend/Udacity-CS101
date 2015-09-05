# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the values
# defined below.    
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second

print 299792458  * 100 * 1.0/1000000000



# Here's a more detailed explanation of the Python code here: 299792458 * 100 * 1.0/1000000000 * 1/2.7 
# The first term is the speed of light in meters per second (this is actually exact - a meter is defined 
# as "the length of the path travelled by light in vacuum during a time interval of 1/299 792 458 of a second.".

# The second term, 100 is the number of centimeters in a meter.

# The third term, 1.0/1000000000 is one billionth. (Note that we need the .0 here (or at least 1.) to make 
# Python do floating point division. Otherwise, 1/1000000000 would evaluate to 0.)

# So, the first three terms in the product compute the distance in centimeters that light travels in one 
# billionth of a second (or one nanosecond). To compute the number of nanoseconds per cycle for my 
# 2.7 GHz processor, the fourth term is 1 / 2.7. Since there are 2.7 Billion cycles per second, there are 2.7 
# cycles per nanosecond, and each cycle takes 1 / 2.7 nanoseconds.


print 299792458  * 100 * 1.0/1000000000 * 1/2.7

speed_of_light = 299792458 # meters per second
cycles_per_second = 2700000000. # 2.7 GHz
billionth = 1.0/1000000000
nanostick = speed_of_light * billionth * 100

print nanostick

# Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle. 
# GV0B3AD95
# GV9847574

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0

print speed_of_light / cycles_per_second

cycle_distance = speed_of_light / cycles_per_second
print cycle_distance * 100

cycles_per_second = 2800000000.0

cycle_distance = speed_of_light / cycles_per_second
print cycle_distance

minutes = 30

minutes = minutes + 1
seconds = minutes * 60
print minutes