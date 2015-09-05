def craw_web(seed):
	tocrawl = [seed]
	crawled = []
	while tocrawl:
		link = tocrawl.pop()
		if link not in crawled:
