import random
'''
1  for snake
-1 for water 
0  for gun
'''
computer  = random.choice([-1,0,1])
you = input("Enter Your Move: ")

youdict = {"s" : 1 , "w" : -1 , "g" : 0}
revdict= {1 : "Snake", -1 : "Water",0:"Gun"}

younum = youdict[you]

print(f"You Chose {revdict[younum]}\n Computer Chose {revdict[computer]}")
if(computer == younum):
    print("Draw")
else:
    if(computer==-1 and younum==0):
        print("You Lose")
    elif(computer==-1 and younum==1):
        print("You Win")


    elif(computer==1 and younum==0):
        print("You Win")
    elif(computer==1 and younum==-1):
        print("You Lose")


    elif(computer==0 and younum==1):
        print("You Lose")
    elif(computer==0 and younum==-1):
        print("You Win")
    else:
        print("Something went Wrong")