# This is a 'Guess the Number' game
import random

# part 1 - computer guesses - you have to find
def pcGuess(n):
    pcNum = random.randint(1, n)
    print(f"\nLet's play 'Guess the Number' game. I'm thinking an integer between 1 and {n}.")
    guesses = 0
    while True:
        guesses += 1
        userNum = int(input("Take a guess: "))
        if userNum > pcNum:
            print(f"Nope, my number is less than {userNum}. ", end='')
        elif userNum < pcNum:
            print(f"Nope, my number is greater than {userNum}. ", end='')
        else:
            break
    print(f"Congrats! You find it with {guesses} guesses.")
    return guesses


# part 2 - your guess - computer has to find 
def userGuess(x):
    input(f"\nThink a number between 1 and {x} and hit enter when you ready...")
    guesses = 0
    # these two variables are limits of randomness
    low = 1
    high = x
    while True:
        guesses += 1
        pcNum = random.randint(low, high)
        userNum = input(f"Is it {pcNum} ? \nif yes type (y), if less type (+), if greater type (-): ".lower())
        if userNum == '+':
            low = pcNum + 1
        elif userNum == '-':
            high = pcNum - 1
        else:
            print(f"I find it with {guesses} guesses.")
            break
    # how many attemps
    return guesses


# part 3 - Who is the winner?! 
def playGuessTheNumber(y=10):
    play = True
    while play:
        user_score = pcGuess(y)
        pc_score = userGuess(y)
        if pc_score>user_score:
            print(f"\nYOU WIN! You find my number with {user_score} guesses. Good job! \n" \
            f"I find your number with {pc_score} guesses.")
        elif pc_score<user_score:
            print(f"\nYou Lose! I find your number with {pc_score} guesses. \n" \
                f"You find my number with {user_score} guesses.")
        else: 
            print(f"\nDRAW! We both found it with {user_score} guesses.")
        # do you want to play agian?
        play = int(input("\nPlay again? yes(1)/no(0): "))


playGuessTheNumber(10) # you can increase the value for playing longer  
