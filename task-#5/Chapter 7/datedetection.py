
import re

testDates = ['31/04/2000', '30/02/1900', '29/02/2000', '30/02/2000', '21/12/4123', '123/12/2222', '41/13/4123', '3a/23/3333']

monthWith30Days = (4,6,9,11)

dateRegex = re.compile(r'(^[0-3]\d)\/([0-1][0-9])\/([1-2]\d{3})')


for testDate in testDates:
    print(f'Checking: {testDate}')
    try:
        day, month, year = dateRegex.findall(testDate)[0]
    except:
        print(f'{testDate} is not a valid date.') 
    if((int(year) % 4) == 0 and (int(year) % 400) == 0 and not (int(year) % 100) != 0 ):
        leapYear = True
    if(int(month) in monthWith30Days and int(day) > 30):
        print(f'{month} has only 30 days') 
    elif(int(month) == 2 and int(day) > 28 and leapYear == False):
        print(f'{month} has only 28 days')
    elif(int(month) == 2 and int(day) > 29 and leapYear == True):
        print(f'{month} has only 29 days')
    elif(int(day) > 31):
        print(f'{month} has only 31 days')
