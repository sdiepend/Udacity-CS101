p = [1, 'a', 3, 'c']
print p
def proc1(p):
	p[0] = p[1]

proc1(p)
print p

# plus creates a new list assigned to a, while p still points to the original list.
def proc2(a):
	a = a + [1]
proc2(p)
print p

def proc3(p):
	q = p
	p.append(3)
	q.pop()
proc3(p)
print p

def proc4(p):
	q = []
	while p:
		q.append(p.pop())
	while q:
		p.append(q.pop())
proc4(p)
print p
