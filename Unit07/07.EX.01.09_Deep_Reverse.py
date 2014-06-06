# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.


def is_list(p):
    return isinstance(p, list)


def deep_reverse(i_list):
    v_list = []
    v_result = []
    v_list += i_list
    if is_list(v_list):
        for i in range(0,len(v_list)):
            v_val = v_list.pop()
            if is_list(v_val):
                v_result.append(deep_reverse(v_val))
            else:
                v_result.append(v_val)
    v_result += v_list
    return v_result


def new_deep_reverse(p):
    if is_list(p):
        result = []
        for i in range(len(p) - 1, -1, -1):
            result.append(new_deep_reverse(p[i]))
        return result
    else:
        return p


#For example,
p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2, 3], 4, [5, 6]]
print deep_reverse(q)
#>>> [ [6, 5], 4, [3, 2], 1]
print q
#>>> [1, [2, 3], 4, [5, 6]]

r = [1, 2, 3, 4, 5, 6]
print new_deep_reverse(r)
print r

p = [1, [2, 3, [4, [5, 6]]]]
print new_deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2, 3], 4, [5, 6]]
print new_deep_reverse(q)
#>>> [ [6, 5], 4, [3, 2], 1]
print q
#>>> [1, [2, 3], 4, [5, 6]]

r = [1, 2, 3, 4, 5, 6]
print new_deep_reverse(r)
print r