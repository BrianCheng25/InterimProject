# import random to get random numbers 
import random

# define function name guess and put x as a variable
def guess(x):
    # random number = Retrun a number between 1 and x
    random_number = random.randint(1, x)
    # guess as a input
    guess = 0

    # when guess not equal to the answer, 
    while guess != random_number:
        #input x to guess
        guess = int(input(f'Guess a number between 1 and {x}: '))
        # print guess 
        print(guess)

        # if guess less than the answer
        if guess < random_number:
            # print guess again
            print('your guess is too low, guess again!')
        # else if guess is greater than the answer
        elif guess > random_number:
            # print guess again
            print('sorry, too high.')
    # otherwise, guess is equal to the answer then return answer and bingo 
    print(f'congrats, {random_number} bingo!')

# call the function and x = 100
guess(100)
