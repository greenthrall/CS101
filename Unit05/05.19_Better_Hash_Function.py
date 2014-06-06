# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.


def hash_string(keyword, buckets):
    v_count = 0
    for v_char in keyword:
        v_count += ord(v_char)
    return v_count % buckets


def new_hash_string(keyword, buckets):
    h = 0
    for c in keyword:
        h = (h + ord(c)) % buckets
    return h


print hash_string('a', 12)
print new_hash_string('a', 12)
#>>> 1
print hash_string('b', 12)
print new_hash_string('b', 12)
#>>> 2
print hash_string('a', 13)
print new_hash_string('a', 13)
#>>> 6
print hash_string('au', 12)
print new_hash_string('au', 12)
#>>> 10
print hash_string('udacity', 12)
print new_hash_string('udacity', 12)
#>>> 11
