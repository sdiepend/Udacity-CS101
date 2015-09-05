# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    # i = 0
    # found = False
    # for e in index:
    #     if e[0] == keyword:
    #         index[i][1].append(url)
    #         found = True
    #     i = i + 1

    # if found == False:
    #     index.append([keyword,[]])
    #     index[i][1].append(url)
    # return index

    for e in index:
        if e[0] == keyword:
            e[1].append(url)
            return index
    index.append([keyword,[url]])
    return index




add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]