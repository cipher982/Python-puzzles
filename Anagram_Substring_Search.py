'''
Given two strings (s,t) determine whether some anagram of t is a substring of s.
'''

def question1(s,t):
	s,t = str(s),str(t)
    s_sort, t_sort = sorted(list(s)),sorted(list(t))
    for letter in range(len(s_sort)):
        window = s_sort[letter: letter+len(t)] 
        if sorted(list(window)) == t_sort:
            return True
    return False

print question1('This is the long string to test jjjjjj 99999999 4ffffff', 'r gst')
# True
print question1('short', '')
# True
print question1('What happens if I attempt a number???', 15)
# False
