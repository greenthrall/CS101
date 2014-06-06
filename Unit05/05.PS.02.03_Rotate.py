# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


def shift_n_letters(letter, n):
    v_result = ord(letter) + n
    if v_result > ord('z'):
        v_result = v_result - ord('z') + ord('a') - 1
    if v_result < ord('a'):
        v_result = v_result + ord('z') - ord('a') + 1
    return chr(v_result)


def rotate(v_string, v_num):
    v_result = ''
    for v_char in v_string:
        if v_char == ' ':
            v_result += ' '
        else:
            v_result += shift_n_letters(v_char, v_num)
    return v_result

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???