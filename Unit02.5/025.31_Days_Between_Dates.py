# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Compensate for leap days. 
# Assume that the birthday and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012 
# you are 1 day old.
#
# Hint
# A whole year is 365 days, 366 if a leap year. 

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

def nextDay(year, month, day):
    if isLeapYear(year):
        if month == 2:
            if day < 29:
                return year, month, day + 1
            else:
                return year, month + 1, 1
        else:
            if day < daysOfMonths[month - 1]:
                return year, month, day + 1
            else:
                if month == 12:
                    return year + 1, 1, 1
                else:
                    return year, month + 1, 1
    else:
        if day < daysOfMonths[month - 1]:
            return year, month, day + 1
        else:
            if month == 12:
                return year + 1, 1, 1
            else:
                return year, month + 1, 1

def dateIsAfter(year1, month1, day1, year2, month2, day2):
    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert dateIsAfter(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsAfter(year2, month2, day2, year1, month1, day1):
        days += 1
        (year1, month1, day1) = nextDay(year1, month1, day1)
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()