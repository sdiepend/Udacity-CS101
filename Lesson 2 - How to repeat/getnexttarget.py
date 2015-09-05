def get_next_target(s):
	start_link = s.find('<a href=')
	start_quote = s.find('"', start_link)
	end_quote = s.find('"', start_quote + 1)
	url = s[start_quote + 1: end_quote]
	return url, end_quote