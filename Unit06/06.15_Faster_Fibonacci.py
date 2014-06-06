#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).


def fibonacci(n):
    v_n1 = 0
    v_n2 = 1
    for i in range(0, n):
        v_n1, v_n2 = v_n2, v_n1 + v_n2
    return v_n1


print fibonacci(36)
#>>> 14930352