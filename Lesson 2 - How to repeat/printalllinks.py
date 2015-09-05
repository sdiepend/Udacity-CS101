def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ''

def get_next_target(page):
    start_link = page.find('<a href=')

    if start_link == -1:
    	return None, 0

    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
    return url, end_quote

def print_all_links(page):
	while True:
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break

print_all_links(get_page('http://www.sdiepend.com'))