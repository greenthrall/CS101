# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(p):
    n1 = len(p)
    if n1 == 0:
        return True
    n2 = len(p[0])
    if n1 != n2:
        return False
    num = 1
    while num <= n1:
        i = 0
        while i < n1:
            colcount = 0
            rowcount = 0
            j = 0
            while j < n1:
                if p[i][j] == p[j][i]:
                    j += 1
                else:
                    return False
            i += 1
        num += 1
    return True

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False

print symmetric([])
#>>> False