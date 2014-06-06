# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000.0 # km per second

def speed_fraction(in_ms,in_km):
    v_time = in_ms
    v_dist = 2.0 * in_km
    v_lat = v_dist / v_time
    return v_lat / speed_of_light * 1000.0

print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?

print speed_fraction(16,20)
#>>> 0.00833333333333