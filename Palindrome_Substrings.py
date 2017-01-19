'''
Using string (a), find the longest palindrome substring contained in (a).
'''

def question2(a):
    a=str(a)
    substrings = [a[x:y+1] for x in xrange(len(a)) for y in xrange(x,len(a))]
    substrings.sort(key=len, reverse=True) # sorts by descending length
    for string in substrings:
        if string == string[::-1]:
            return string
            break
            
print question2('sdfljksksdklsdfkjskdsfsdfsfsfdsdfsdldfjsldkfjsldfjsdlkjfdslkfjsdlkfjdf')
# sdfsfsds
print question2('')
# None
print question2(9449847847584754 ** 85)
# 4814184
