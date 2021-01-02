import random
number = random.randint(1,9)
chances = 0
print('guess a number between 1 and 9')
while chances<5:
    guess = int(input('enter a number'))
    if guess==number:
        print('YOU WON')
        break     
    elif guess<number :
        print('Your guess is LOW ')
    else :
        print('Your guess is HIGH')
    chances=chances+1
if not chances<5 :
    print('YOU LOOSE the number is:',number)
