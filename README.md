# Exercises-From-Books-Read

### Date Detection 
Answer - *date_detection.py*

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
Answer - *password_detection.py*

Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase charac-
ters, and has at least one digit. You may need to test the string against mul-
tiple regex patterns to validate its strength.


### Phone Number and Email Address
Answer - *phoneAndEmail.py*

Say you have the boring task of finding every phone number and email
address in a long web page or document. If you manually scroll through
the page, you might end up searching for a long time. But if you had a pro-
gram that could search the text in your clipboard for phone numbers and
email addresses, you could simply press ctrl-A to select all the text, press
ctrl -C to copy it to the clipboard, and then run your program. It could
replace the text on the clipboard with just the phone numbers and email
addresses it finds.

### Backing up a folder into a ZIP File
Answer - *backupToZip.py*

Say you’re working on a project whose files you keep in a folder named
*C:\AlsPythonBook*. You’re worried about losing your work, so you’d like
to create ZIP file “snapshots” of the entire folder. You’d like to keep
different versions, so you want the ZIP file’s filename to increment each
time it is made; for example, AlsPythonBook_1.zip, AlsPythonBook_2.zip,
AlsPythonBook_3.zip, and so on.

### Renaming Files with American-Style Dates to European-Style Dates
Answer - *renameDates.py*

Say your boss emails you thousands of files with American-style dates
(MM-DD-Y Y Y Y) in their names and needs them renamed to European-
style dates (DD-MM-Y Y Y Y). This boring task could take all day to do by
hand! 

### Mad Libs 

Answer - *mad_libs.py*

Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events. The program would find these occurrences and prompt the user to replace them.

*Enter an adjective:*
*silly*

*Enter a noun:*
*chandelier*

*Enter a verb:*
*screamed*

*Enter a noun:*
*pickup truck*

The following text file would then be created:
The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.


The results should be printed to the screen and saved to a new text file


### Regex Search

Answer - *regex_search.py*

Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.

### Generating Random Quiz Files

Answer - *randomQuizGenerator.py*

Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. Fortunately, you know some Python.

1. Creates 35 different quizzes
2. Creates 50 multiple-choice questions for each quiz, in random order
3. Provides the correct answer and three random wrong answers for each
question, in random order
4. Writes the quizzes to 35 text files
5. Writes the answer keys to 35 text files

###  Sandwich Maker
Answer - *sandwich_maker.py*

Write a program that asks users for their sandwich preferences. The pro-
gram should use PyInputPlus to ensure that they enter valid input, such as:
• Using inputMenu() for a bread type: wheat, white, or sourdough.
• Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.•
• Using inputYesNo() to ask if they want cheese.
• If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
• Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
• Using inputInt() to ask how many sandwiches they want. Make sure this
number is 1 or more.

Come up with prices for each of these options, and have your program
display a total cost after the user enters their selection.


### 2048

Answer - *2048.py*

2048 is a simple game where you combine tiles by sliding them up, down,
left, or right with the arrow keys. You can actually get a fairly high score
by repeatedly sliding in an up, right, down, and left pattern over and over
again. Write a program that will open the game at https://gabrielecirulli​
.github.io/2048/ and keep sending up, right, down, and left keystrokes to
automatically play the game.


### Selective Copy

Answer - *selective_copy.py*

Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.