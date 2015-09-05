countdown = 10

while countdown >= 0:
	print countdown
	countdown = countdown -1

print "Option 1"
countdown = 10
while countdown >= 0:
	if False:
		break
	print countdown
	countdown = countdown - 1

print "Option 2"
countdown = 10
while countdown >= 0:
	print countdown
	countdown = countdown - 1
	break

print "Option 3"
countdown = 10
while True:
	if countdown >= 0:
		break
	print countdown
	countdown = countdown -1

print "Option 4"
countdown = 10
while countdown >= 0:
    print countdown
    countdown = countdown - 1  
    if countdown >= 0:
        print countdown
        countdown = countdown - 1
    else:
		break