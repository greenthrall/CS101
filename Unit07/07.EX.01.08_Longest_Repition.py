# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.


def longest_repetition(i_list):
    if i_list == []:
        return None
    v_result = [i_list[0], 1]
    v_curr = ['', 0]
    for v_val in i_list:
        if v_val == v_curr[0]:
            v_curr[1] += 1
            if v_curr[1] > v_result[1]:
                v_result = v_curr
        else:
            v_curr = [v_val, 1]
    return v_result[0]


def new_longest_repetition(input_list):
    best_element = None
    length = 0
    current = None
    current_length = 0
    for element in input_list:
        if current != element:
            current = element
            current_length = 1
        else:
            current_length += 1
        if current_length > length:
            best_element = current
            length = current_length
    return best_element


#For example,
print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
print new_longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
print new_longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
print new_longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
print new_longest_repetition([])
# None

