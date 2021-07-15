# File name: HomeWork1.py
# Author Name: Ben Sottile
# Date: 09/05/2019
# Description: This code will print my bio to the console

# Full Disclaimer: I found out how to do this online. The Class color contains mulitiple methods
# That when used in concatination, format the text utilzing unicode. It stops formattting when the End
# method is invoked.
class color:
     DARKCYAN = '\033[36m'
     BLUE = '\033[94m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     RED = '\033[91m'
     BOLD = '\033[1m'
     UNDERLINE = '\033[4m'
     END = '\033[0m'
     PURPLE = '\033[95m'
     CYAN = '\033[96m'

# However, I did in fact create these functions

def boldtext(mytext):
    print(color.BOLD + mytext + color.END )
boldtext("Ben Sottile's Bio")
print('''Hi, I'm''' + color.BOLD + color.RED + ' Ben Sottile' + color.END + ''',
 and I'm a ''' + color.GREEN + '''Freshmen '''+ color.END + color.BLUE + color.UNDERLINE + '''Computer Science Major'''
  + color.END + ''' with aspirations to ''' + color.BOLD + '''double major ''' + color.END + '''in ''' + color.YELLOW + '''small business
 management and entrepreneurship. ''' + color.END + '''I have taken a prior class in ''' + color.PURPLE + '''Scratch''' + color.END + ''' in '''+ color.UNDERLINE +'''middle school '''+ color.END + '''which
 is an educational block programming language and as I mentioned in my high school junior year 
 I took ''' + color.BLUE + color.UNDERLINE + '''AP Computer Science''' + color.END + ''' which is the basics of Java. I have '''+ color.UNDERLINE+ color.BOLD + '''ZERO''' + color.END + ''' experience with the python 
 language and will be learning from scratch. I would like to come out of this semester with
 knowledge of the basics of Python and become a more''' + color.DARKCYAN + ''' confident programmer. '''+ color.END + '''I would really like
 to build a foundation to which I can put the rest of my ''' + color.BLUE + color.UNDERLINE + '''COM SCI ''' + color.END + '''classes on.''')