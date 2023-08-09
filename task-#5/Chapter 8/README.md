1. PyInputPlus doesnot come with the Python Standard Library, we must install it separately using Pip.
2. The as pyip code in the import statement saves us from typing pyinputplus each time we want to call a PyInputPlus function. Instead we can use the shorter pyip name.
3. inputInt() function accepts integer value( 23,45 ..) and inputFloat() function accepts float values(3.14,4.5 and so on...)
4.  response = pyip.inputInt('Enter a num: ' , min=0 , lessThan=100)
5. The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input.
6. limit=3 allows the user to prompt input 3 times max because blanck input is invalid.  
7. If the blank input is entered 3 times then the default  value will be displayed that is 'hello'.
