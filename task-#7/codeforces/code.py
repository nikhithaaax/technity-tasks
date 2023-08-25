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


#3

def main():
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))

    kscore = scores[k - 1]  

    
    count = 0
    for score in scores:
        if score >= kscore and score > 0:
            count = count+1

    print(count)

if __name__ == "__main__":
    main()


#4

def main():
    n = int(input("Enter no. of operations : "))  
    x = 0  

    for _ in range(n):
        operation = input("Enter operation/s : ")
        if "++" in operation:
            x = x+1
        else:
            x = x-1

    print("Result : ",x)

if __name__ == "__main__":
    main()


#5

def main():
    team=input()
    
    consecutivezeros=0
    consecutiveones=0
    is_dangerous=False
    
    for char in team:
        if char=="1":
            consecutiveones += 1 
            consecutivezeros = 0
        else:
            consecutivezeros += 1 
            consecutiveones = 0
        if consecutiveones >=7 or consecutivezeros >=7:
            is_dangerous=True
            break
    
    
    if is_dangerous:
        print("YES")
        
    else:
        print("NO")
    
            

if __name__ == "__main__":
    main()  
    


