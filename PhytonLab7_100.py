x = 1
while(x<300):
    print x
    x = x + 2
    
    
myList = [1,2,3,4,5,6,7,8,9,10]
index = 0
while (index < len(myList)):
    print myList[index]
    index = index + 1
    
    
import random
rand = random.randint(0,50)
userInput = -1
while(rand != userInput):
    userInput = int(raw_input())
    if rand > userInput:
        print "Too Low!"
    if rand < userInput:
        print "Too High!"
    if rand == userInput:
        print "Congrats!!"
        