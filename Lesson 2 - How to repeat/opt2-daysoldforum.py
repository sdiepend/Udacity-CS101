MONTHS_OF_YEAR = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTHS_OF_LEAPYEAR = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def daysbetweendates(year1, month1, day1, year2, month2, day2):
	days = 0
	days_leap = 0
	days_normal = 0

	for x in range(0, len(MONTHS_OF_LEAPYEAR)):
	    days_leap += MONTHS_OF_LEAPYEAR[x]

	# print days_leap
	for x in range(0, len(MONTHS_OF_YEAR)):
	    days_normal += MONTHS_OF_YEAR[x]

	for year in range(year2 - year1):
	    days += days_leap if is_leapyear(year) else days_normal
	    print(year)
	    print("executed")

	for month in range(month1, month2):
	    if is_leapyear(year2 - year1):
	        days += MONTHS_OF_LEAPYEAR[month]
	    else:
	        days += MONTHS_OF_YEAR[month]

	delta  = day2 - day1
	days  += delta  and days if days  > 0 else 0
	print(days)
	return days

def is_leapyear(year):
	if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
		return True
	else:
		return False

	# print(daysbetweendates(2012, 1, 1, 2012, 2, 28)) # 58
	# print(daysbetweendates(2012, 1, 1, 2012, 3, 1)) # 60
	# print(daysbetweendates(2011, 6, 30, 2012, 6, 30)) # 366
	# print(daysbetweendates(2011, 1, 1, 2012, 8, 8)) # 585
	# print(daysbetweendates(1900, 1, 1, 1999, 12, 31)) # 36523

def test():
	test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
	((2012, 1, 1, 2012, 3, 1), 60),
	((2011, 6, 30, 2012, 6, 30), 366),
	((2011, 1, 1, 2012, 8, 8), 585),
	((1900, 1, 1, 1999, 12, 31), 36523)]
	for (args, answer) in test_cases:
		result = daysbetweendates(*args)
		if result != answer:
			print("Test with data:", args, "failed")
		else:
			print("Test case passed!")

test()