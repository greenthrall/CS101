# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            return n1
    if n2 > n3:
        return n2
    else:
        return n3

def bigger(n1, n2):
    if n1 > n2:
        return n1
    return n2

def new_biggest(n1, n2, n3):
    return bigger(bigger(n1, n2), n3)

print biggest(3, 6, 9)
print new_biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
print new_biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
print new_biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
print new_biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
print new_biggest(9, 3, 9)
#>>> 9