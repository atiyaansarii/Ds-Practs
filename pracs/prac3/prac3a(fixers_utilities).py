import string

#1 Removing leading or lagging spaces from a data entry
print('1.Removing leading or lagging spaces from a data entry')
baddata = "      Data with too many spaces is too bad!!!!       "
print('>', baddata, '<')
Cleandata = baddata.strip()
print('>', Cleandata, '<')

#2 Removing nonprintable characters from a data entry
print('2.Removing nonprintable characters from a data entry')
printable = set(string.printable)
baddata = "Data\x00Science with\x02 funny characters from a data entry"
Cleandata = ''.join(filter(lambda x: x in string.printable, baddata))
print('Bad data :', baddata)
print('Clean data :', Cleandata)

#3 Reformatting data entry to match specific formatting criteria
print('3.Reformatting data entry to match specific formatting criteria')
import datetime as dt
baddate = dt.date(2019, 10, 21)
baddata = format(baddate, '%Y-%m-%d')
print("The date is: ", baddata)
gooddate = dt.datetime.strptime(baddata, '%Y-%m-%d')
gooddata = format(gooddate, '%d %B %Y')
print("Reformatted Date:", gooddata)
