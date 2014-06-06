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
# If you know how many days it is from 1 Jan until a certain date,
# you also know how many days there are left from that date until 31 Dec.

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year%400 == 0:
        return 366
    if year%100 == 0:
        return 365
    if year%4 == 0:
        return 366
    else:
        return 365

def dayOfYear(year, month, day):
    days = 0
    i = 1
    while i <= month:
        if isLeapYear(year) == 366:
            if i == month:
                days = days + day
                return days
            if i == 2:
                days = days + 29
            else:
                days = days + daysOfMonths[i-1]
        else:
            if i == month:
                days = days + day
                return days
            else:
                days = days + daysOfMonths[i-1]
        i = i + 1


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    daycount = 0
    days1 = dayOfYear(year1, month1, day1)
    days2 = dayOfYear(year2, month2, day2)
    if year1 == year2:
        daycount = days2 - days1
        return daycount
    else:
        if isLeapYear(year1) == 366:
            daycount = 366 - days1
            year1 = year1 + 1
        else:
            daycount = 365 - days1
            year1 = year1 + 1
        while year1 < year2:
            if isLeapYear(year1) == 366:
                daycount = daycount + 366
            else:
                daycount = daycount + 365
            year1 = year1 + 1
        return daycount + days2

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed", result
        else:
            print "Test case passed!"

test()
