def bad_hash_string(keyword, buckets):
    return ord(keyword[0]) % buckets

def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)
    return results

# SPOILER: Better hash function of the next video
def hash_string(keyword,buckets):
    sum = 0
    for l in keyword:
        sum += ord(l)
    bucketnr = sum % buckets
    return bucketnr

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

words = get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split()

#counts = test_hash_function(bad_hash_string, words, 12)
counts = test_hash_function(hash_string, words, 12)
print(counts)