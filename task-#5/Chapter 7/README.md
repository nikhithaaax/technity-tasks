1. nameOfRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
2. Raw strings are often used when creating regex objects to simplify the process of writing and reading regular expression patterns by avoiding unnecessary escaping of characters.
3. search() method searches the string it is passed for any matches to the regex. The search() method will return None if the regex pattern is not found in the string. If found, the search() method returns a match object.
4. By using group() method we can get the actual string that matches the pattern from a Match object.
5. group(0) will return entire matched text. While group(1) will return the first set of parenthesis(\d\d\d) and group(2) will return second set of parenthesis (\d\d\d-\d\d\d\d)
6. We need to escape them with backslash.For parentheses '\\(' or  '\\)' and for period '\\.'
7. When findall() method called on a regex with no groups , it returns a list of string matches. Whereas , when called on a regex that has groups , it returns a list of tuples of strings.
8. The | character is called a pipe. It is used to match one of many expressions.For example, the regular expression r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'.
9. What two things does the ? character signify in regular expressions?
10. The question mark can have two meanings in regular expressions: declaring a non-greedy match or flagging an optional group.
11. {3} will match exactly 3 instances of the specified group while {3,5} will match 3 to 5 instances.
12. \d represents any numeric digit from 0 to 9. \w represents any letter, numeric digit, or the underscore character. \s represents any space, tab, or newline character.
13. \D represents any character that is not a numeric digit from 0 to 9. \W represents any character that is not a letter, numeric digit, or the underscore character. \S represents any character that is not a space, tab, or newline.
14. .* uses greedy mode: matches longest string possible. .*? used non-greedy mode: matches shortest string possible.
15. nameOfRegex = re.compile(r'[0-9a-z]')
16. To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile().
17. In a regular expression, the . character (period) is a special metacharacter that matches any single character except a newline (\n).However, when you pass the re.DOTALL flag as the second argument to re.compile(),it changes it's behavior. The re.DOTALL flag, causes the . character to match any character, including newline characters (\n).
18. 'X drummers, X pipers, five rings, X hens'
19. Passing re.VERBOSE as the second argument to re.compile() in Python allows you to write more human-readable and well-organized regular expressions by ignoring whitespace and comments.
20. (^\d{1,3}(,\d{3})*$)
21. r'^[A-Z][a-z]*\sWatanabe$'
22. r'^(Alice|Bob|Carol)\s+(eats|pets|throws)\s+(apples|cats|baseballs)\.$'


