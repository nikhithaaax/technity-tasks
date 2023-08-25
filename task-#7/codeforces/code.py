#1

import math

def theatresquare(n, m, a):
    
    r = math.ceil(n / a)
    c = math.ceil(m / a)
    flagstones = r * c
    return flagstones


n, m, a = map(int, input("Enter n, m, and a: ").split())

result = theatresquare(n, m, a)
print("Number of flagstones required:", result)

#2

word=input("Enter a word : ")
def abbrevated_word(word):
	if len(word) > 10:
		return word[0] + str(len(word) - 2) + word[-1]
	else: 
		return word
		
result=abbrevated_word(word)
print("Sorted word is : ",result )
