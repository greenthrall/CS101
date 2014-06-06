# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(p):
    ret_val = 0
    for i in p:
        if i > ret_val:
            ret_val = i
    return ret_val

print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0