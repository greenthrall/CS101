# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. Itcan 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
    return match, replacement


def apply_converter(converter, string):
    while converter[0] in string:
        v_start = string.index(converter[0])
        v_end = v_start + len(converter[0])
        string = string[:v_start] + converter[1] + string[v_end:]
    return string


def new_make_converter(match, replacement):
    return [match, replacement]


def new_apply_converter(converter, string):
    previous = None
    while previous != string:
        previous = string
        position = string.find(converter[0])
        if position != -1:
            string = string[:position] + converter[1] + string[position + len(converter[0]):]
    return string
        
# For example:

c1 = make_converter('aa', 'a')
print apply_converter(c1, 'aaaa')
c1 = new_make_converter('aa', 'a')
print new_apply_converter(c1, 'aaaa')
#>>> a

c = make_converter('aba', 'b')
print apply_converter(c, 'aaaaaabaaaaa')
c = new_make_converter('aba', 'b')
print new_apply_converter(c, 'aaaaaabaaaaa')
#>>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever).
