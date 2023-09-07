"""
    - detects dates in DD/MM/YYYY
    - days : 0 - 31, month: 0 - 12, years: 1000 - 2999
    - store into vars month, day and year
    - write code to detect if it is a valid date
"""

import re
# from faker import Faker

dateRegex = re.compile(r'''
    (0[1-9]|1[0-9]|2[0-9]|3[01])  # Day: 01-31
    /
    (0[1-9]|1[0-2])  # Month: 01-12
    /
    (1[0-9]{3}|2[0-9]{3})  # Year: 1000-2999
''', re.VERBOSE)

test = """
    07/01/3000
    24/10/2008
    25/10/2004
    16/09/1988
    26/06/1980
"""
found_all = dateRegex.findall(test)
valid_months = {
    30: {
        '04': "April",
        '06': "June",
        '09': "September",
        '11': "November"
    },
    28: "February",
}

for date in found_all:
    day, month, year = date.split("/")

    bool_year = 1000 <= int(year) <= 2999
    bool_month = 0 < int(month) <= 12
    bool_day = 0 < int(day) <= 31

    if month in valid_months[30]:
        check = int(day) <= 30
        if not check:
            raise ValueError("error")

    elif month == '02':
        if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0):
            check = int(day) <= 29  # Leap year
        else:
            check = int(day) <= 28  # Non-leap year

        if not check:
            raise ValueError("error")

    if bool_day and bool_month and bool_year:
        if len(day) == 1:
            day = '0' + day

        print("end")
