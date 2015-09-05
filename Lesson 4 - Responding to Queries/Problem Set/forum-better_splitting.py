#Forum question: https://discussions.udacity.com/t/lesson-4-problem-set-better-splitting/26817/1

def split_string(source,splitlist):
    output = []
    counter = 0
    for word in source:
        for separator in splitlist:
          if word == separator:
            stop_counter = splitlist.index(separator)
            print "stop_counter === ",stop_counter
            output.append(source[counter:stop_counter])
            counter = stop_counter + 1
    return output

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out

#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out

#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']