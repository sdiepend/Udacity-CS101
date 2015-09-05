# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

# def longest_repetition(list):
#     repetition = {}
#     before = ""
#     for e in list:
#         if e == before:
#             repetition[e] = repetition[e] + 1
#         else:
#             repetition[e] = 1
#         before = e
#     biggest = 0
#     longest_repetition = None
#     for e in repetition:
#         if repetition[e] > biggest:
#             biggest = repetition[e]
#             longest_repetition = e
#     return longest_repetition

# My solution
def longest_repetition(list):
    before = None
    longest_repetition = None
    most_repititons = 0
    number_of_repetitions = 1
    for e in list:
        if e == before:
            number_of_repetitions = number_of_repetitions + 1
        else:
            number_of_repetitions = 1
        if number_of_repetitions > most_repititons:
            longest_repetition = e
            most_repititons = number_of_repetitions
        before = e

    return longest_repetition

# Udacity solution
def longest_repetition2(input_list):
    best_element = None
    length = 0
    current = None
    current_length = 0
    for element in input_list:
        if current != element:
            current = element
            current_length = 1
        else:
            current_length = current_length + 1
        if current_length > length:
            best_element = current
            length = current_length
    return best_element



#For example,
print longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])
print longest_repetition2([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]])

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
print longest_repetition2([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
print longest_repetition2([1,2,3,4,5])
# 1

print longest_repetition([])
print longest_repetition2([])
# None



