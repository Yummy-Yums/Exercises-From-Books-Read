# Exercises-From-Books-Read

### Date Detection 
Answer - date_detection.py

Write a regular expression that can detect dates in the DD/MM/YYYY for-
mat. Assume that the days range from 01 to 31, the months range from 01
to 12, and the years range from 1000 to 2999. Note that if the day or month
is a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each
month or for leap years; it will accept nonexistent dates like 31/02/2020 or
31/04/2021. Then store these strings into variables named month, day, and
year, and write additional code that can detect if it is a valid date. April,
June, September, and November have 30 days, February has 28 days, and
the rest of the months have 31 days. February has 29 days in leap years.
Leap years are every year evenly divisible by 4, except for years evenly divis-
ible by 100, unless the year is also evenly divisible by 400. Note how this cal-
culation makes it impossible to make a reasonably sized regular expression

### Strong Password Detection
Answer - password_detection.py

Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase charac-
ters, and has at least one digit. You may need to test the string against mul-
tiple regex patterns to validate its strength.


### Phone Number and Email Address
Answer - phoneAndEmail.py

Say you have the boring task of finding every phone number and email
address in a long web page or document. If you manually scroll through
the page, you might end up searching for a long time. But if you had a pro-
gram that could search the text in your clipboard for phone numbers and
email addresses, you could simply press ctrl-A to select all the text, press
ctrl -C to copy it to the clipboard, and then run your program. It could
replace the text on the clipboard with just the phone numbers and email
addresses it finds.