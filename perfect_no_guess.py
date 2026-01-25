import random
r=random.randint(1,100)
count=0
n=-1
while r!=n:
    count+=1
    n=int(input("Guess a number: "))
    if n==r:
        print(end="")
    elif n>r:
        print("lower no please")  
    else:
        print("higher no please")

print(f"You guessed your number in {count} time")