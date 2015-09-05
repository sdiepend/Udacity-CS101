# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
	hashtable = []
	i = 0
	while i < nbuckets:
		hashtable.append([])
		i = i + 1
	# hashtable[4] = "HA"
	return hashtable

print(make_hashtable(10))

def make_hashtable_better(nbuckets):
	table = []
	for unused in range(0, nbuckets):
		table.append([])
	return table

def make_hastable_NOT(nbuckets):
	return [[]] * nbuckets


