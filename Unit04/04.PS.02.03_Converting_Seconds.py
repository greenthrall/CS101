# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3

def convert_seconds(in_val):
    v_hr = 0
    v_min = 0
    v_sec = 0
    o_hr = 'hours'
    o_min = 'minutes'
    o_sec = 'seconds'
    while in_val > 0:
        if in_val >= 1:
            if in_val >= 60:
                if in_val >= 3600:
                    v_hr += 1
                    in_val -= 3600
                else:
                    v_min += 1
                    in_val -= 60
            else:
                v_sec += 1
                in_val -= 1
        else:
            v_sec += in_val
            in_val = 0
    if v_hr == 1:
        o_hr = 'hour'
    if v_min == 1:
        o_min = 'minute'
    if v_sec == 1:
        o_sec = 'second'
    return str(v_hr) + ' ' + o_hr + ', ' + str(v_min) + ' ' + o_min + ', ' + str(v_sec) + ' ' + o_sec
    
print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

print convert_seconds(0)