import re

def stripfn(string,spc):
  
    ask = input("do you wasnt to strip any character ? Y OR N: ")
    if ask=="N":
        return string.strip()
    else:
        spc=input("enter the character to be removed: ")
        stringregex=re.compile(spc)
        return stringregex.sub("",string)
spc=""
        
string=input("enter a string : ")
print(stripfn(string,spc))
