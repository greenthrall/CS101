# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(in_list,in_test):
    count = 0
    for e in in_list:
        if e == in_test:
            return count
        else:
            count += 1
    return -1

def while_find_element(in_list,in_test):
    i = 0
    while i < len(in_list):
        if in_list[i] == in_test:
            return i
        i += 1
    return -1

print find_element([1,2,3],3)
print while_find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
print while_find_element(['alpha','beta'],'gamma')
#>>> -1