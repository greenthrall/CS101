# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def download_time(i_file_size,i_file_unit,i_bandwidth,i_bandwith_unit):
    v_size_list = [[2.0 ** 10, 'kb'], [2.0 ** 10 * 8, 'kB'],
                   [2.0 ** 20, 'Mb'], [2.0 ** 20 * 8, 'MB'],
                   [2.0 ** 30, 'Gb'], [2.0 ** 30 * 8, 'GB'],
                   [2.0 ** 40, 'Tb'], [2.0 ** 40 * 8, 'TB']]
    i = 0
    j = 0
    v_hr = 0
    v_min = 0
    v_sec = 0
    o_file_unit = 0
    o_bandwith_unit = 0
    o_val = 0
    o_hr = 'hours'
    o_min = 'minutes'
    o_sec = 'seconds'
    while i < len(v_size_list):
        if i_file_unit == v_size_list[i][1]:
            o_file_unit = i
        i = i + 1
    while j < len(v_size_list):
        if i_bandwith_unit == v_size_list[j][1]:
            o_bandwith_unit = j
        j = j + 1
    o_val = i_file_size / v_size_list[o_bandwith_unit][0] * v_size_list[o_file_unit][0] / i_bandwidth
    while o_val > 0:
        if o_val >= 1:
            if o_val >= 60:
                if o_val >= 3600:
                    v_hr += 1
                    o_val -= 3600
                else:
                    v_min += 1
                    o_val -= 60
            else:
                v_sec += 1
                o_val -= 1
        else:
            v_sec += o_val
            o_val = 0
    if v_hr == 1:
        o_hr = 'hour'
    if v_min == 1:
        o_min = 'minute'
    if v_sec == 1:
        o_sec = 'second'
    return str(v_hr) + ' ' + o_hr + ', ' + str(v_min) + ' ' + o_min + ', ' + str(v_sec) + ' ' + o_sec
    


print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
