import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    elif int(guess) > number :
        print("Your guess {}. is High. Try lower.".format(guess))
    else:   
        print("Your guess {}. is Low. Try High.".format(guess))