import random 
import time 

numberOfQuestions=10
chances=3
startTime=0 
correctAnswers=0 

i=0 

for questionNumber in range(numberOfQuestions):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    
    result = num1*num2
    
    while(chances>0):
        
        if(startTime==0):
            startTime=time.time()
        while(True):
            answer=input(f"{questionNumber+1}) {num1}*{num2} = ? ")
            try:
                answer=int(answer)
                break
            except ValueError:
                print("This is not a number, please try again")
        if(answer==result):
            print("Correct Answer!!")
            
            correctAnswers=correctAnswers+1
            time.sleep(1)
            break
        elif((time.time()-startTime)>=8):
            print("Sorry time's up")
            break
        else:
            print("Incorrect Anwer try again!!")
            chances=chances-1
            questionNumber=questionNumber+1

print("Your Score is %d  "%(correctAnswers))
