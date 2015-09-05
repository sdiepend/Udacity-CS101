# https://discussions.udacity.com/t/indexerror-list-index-out-of-range-but-it-isnt-please-help/25631/2

def freq_analysis(message):
    freq_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    y = -1
    for e in message:
        x = -1
        while e != freq_list[x]:
            x = x + 1
        if e == freq_list[x]:
            count[x] = (count[x] + 1)
    # issues lies within this piece of code
    while y < (len(count)):
        y = y + 1
        count[y] = count[y] / len(message)
    return count

#Tests

print freq_analysis("abcd")
# >>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]