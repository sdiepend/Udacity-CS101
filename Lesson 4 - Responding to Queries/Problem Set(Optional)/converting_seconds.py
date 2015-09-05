# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(n):
    str_hours = " hours"
    str_min = " minutes"
    str_sec = " seconds"

    hour, rest = n / 3600, n % 3600
    hour = int(hour)
    if hour == 1:
        str_hours = " hour"

    minute = rest / 60
    minute = int(minute)
    if minute == 1:
        str_min = " minute"

    sec = rest % 60
    if sec == 1:
        str_sec = " second"

    return str(hour) + str_hours + ", " + str(minute) + str_min + ", " + str(sec) + str_sec


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

print convert_seconds(7188)