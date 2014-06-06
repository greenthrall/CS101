# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is 
# a dictionary and the second a string. The string is a valid date in 
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".

# Hint: int('12') converts the string '12' to the integer 12.


def date_converter(i_lang, i_date):
    v_count = 0
    while '/' in i_date:
        v_start = i_date.index('/')
        if v_count == 0:
            v_mon = i_date[:v_start]
            v_count += 1
        else:
            v_day = i_date[:v_start]
            v_year = i_date[v_start+1:]
        i_date = i_date[v_start+1:]
    return v_day + ' ' + i_lang[int(v_mon)] + ' ' + v_year


def new_date_converter(language, date):
    first = date.find('/')
    month = date[:first]
    second = date.find('/', first + 1)
    day = date[first + 1:second]
    year = date[second + 1:]
    return day + " " + language[int(month)] + " " + year


def new_date_converter2(language, date):
    month, day, year = date.split('/')
    return day + " " + language[int(month)] + " " + year

print date_converter(english, '5/11/2012')
print new_date_converter(english, '5/11/2012')
print new_date_converter2(english, '5/11/2012')
#>>> 11 May 2012

print date_converter(english, '5/11/12')
print new_date_converter(english, '5/11/12')
print new_date_converter2(english, '5/11/12')
#>>> 11 May 12

print date_converter(swedish, '5/11/2012')
print new_date_converter(swedish, '5/11/2012')
print new_date_converter2(swedish, '5/11/2012')
#>>> 11 maj 2012

print date_converter(swedish, '12/5/1791')
print new_date_converter(swedish, '12/5/1791')
print new_date_converter2(swedish, '12/5/1791')
#>>> 5 december 1791
