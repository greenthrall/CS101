###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day == 30:
        if month == 12:
            year = year + 1
            month = 1
            day = 1
        else:
            month = month + 1
            day = 1
    else:
        day = day + 1
    return year, month, day

def newnextDay(year, month, day):
    """Warning: this version incorrectly assumes all months have 30 days!"""
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

print nextDay(1999, 12, 30)
print newnextDay(1999, 12, 30)
# >>> 2000, 1, 1
print nextDay(2013, 01, 30)
print newnextDay(2013, 01, 30)
# >>> 2013, 2, 1
print nextDay(2012, 12, 30)
print newnextDay(2012, 12, 30)
# >>> 2013, 1, 1