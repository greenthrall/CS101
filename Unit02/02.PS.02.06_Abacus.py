#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_row(s):
    if s == '0':
        ret_val = '|00000*****   |'
    if s == '1':
        ret_val = '|00000****   *|'
    if s == '2':
        ret_val = '|00000***   **|'
    if s == '3':
        ret_val = '|00000**   ***|'
    if s == '4':
        ret_val = '|00000*   ****|'
    if s == '5':
        ret_val = '|00000   *****|'
    if s == '6':
        ret_val = '|0000   0*****|'
    if s == '7':
        ret_val = '|000   00*****|'
    if s == '8':
        ret_val = '|00   000*****|'
    if s == '9':
        ret_val = '|0   0000*****|'
    return ret_val

def print_abacus(value):
    v_value = '0000000000' + str(value)
    v_value = v_value[-10:]
    v_len = len(v_value)
    i,j = 9,0
    while i >= 0:
        print print_row(v_value[j])
        i = i - 1
        j = j + 1

def new_print_abacus(value):
    n = 1000000000
    while n >= 1:
        print '|00000*****'[ :11 - value / n] + '   ' + '|00000*****'[11 - value / n:] + '|'
        n, value = n / 10, value%n

###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
new_print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |

print "Abacus showing 12345678:"
print_abacus(12345678)
new_print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|

print "Abacus showing 1337:"
print_abacus(1337)
new_print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|