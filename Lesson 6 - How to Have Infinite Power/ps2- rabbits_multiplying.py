# Rabbits Multiplying

# A (slightly) more realistic model of rabbit multiplication than the Fibonacci
# model, would assume that rabbits eventually die. For this question, some
# rabbits die from month 6 onwards.
#
# Thus, we can model the number of rabbits as:
#
# rabbits(1) = 1 # There is one pair of immature rabbits in Month 1
# rabbits(2) = 1 # There is one pair of mature rabbits in Month 2
#
# For months 3-5:
# Same as Fibonacci model, no rabbits dying yet
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2)
#
#
# For months > 5:
# All the rabbits that are over 5 months old die along with a few others
# so that the number that die is equal to the number alive 5 months ago.
# Before dying, the bunnies reproduce.
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)
#
# This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ...
#
# Define a procedure rabbits that takes as input a number n, and returns a
# number that is the value of the nth number in the rabbit sequence.
# For example, rabbits(10) -> 35. (It is okay if your procedure takes too
#                                long to run on inputs above 30.)

#My solution
def rabbits(n):
    if n == 0 or n == 1:
        return n
    elif n < 5:
        return (rabbits(n-1) + rabbits(n-2))
    else:
        return (rabbits(n-1) + rabbits(n-2) - rabbits(n-5))

#Udacity's video sotultion
def rabbits2(n):
    if n < 1: #no rabbits dead yet
        return 0
    else:
        if n == 0 or n == 1:
            return n
        else:
            return (rabbits(n-1) + rabbits(n-2) - rabbits(n-5))


print rabbits(10)
print rabbits2(10)
#>>> 35

s = ""
for i in range(1,30):
    s = s + str(rabbits(i)) + " "
print s
#>>> 1 1 2 3 5 7 11 16 24 35 52

