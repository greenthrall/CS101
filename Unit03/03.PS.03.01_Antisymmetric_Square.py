# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(p):
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
                if p[i][j] == -p[j][i]:
                    j += 1
                else:
                    return False
            i += 1
        num += 1
    return True

# Test Cases:
print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
