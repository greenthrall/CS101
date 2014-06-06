# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(search, target):
    retval = search.find(target)
    n = 0
    while search.find(target, n) != -1:
        n = n + 1
    return n - 1

def new_find_last(search, target):
    last_pos = -1
    while True:
        pos = search.find(target, last_pos + 1)
        if pos == -1:
            return last_pos
        last_pos = pos

print find_last('aaaa', 'a')
print new_find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
print new_find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
print new_find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
print new_find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
print new_find_last("222222222", "")
#>>> 9

print find_last("", "3")
print new_find_last("", "3")
#>>> -1

print find_last("", "")
print new_find_last("", "")
#>>> 0
