from random import randint

ease=10
hard=5

guess_ans=False

def comp_num(rand_num,ease_guess,turns):
    if rand_num > ease_guess:
        print("Too Low")
        
        return turns-1
    elif rand_num < ease_guess:
        print("Too High")
        
        return turns-1
    elif rand_num==ease_guess:
        print(f"You got it! The answer was {rand_num}.")
    

def set_diff():
    diffculty=input("Choose diffculty type 'Easy' or 'Hard'\n").lower()
    if diffculty == "easy":
        return ease
    elif diffculty=='hard':
        return hard
    

def stsrt_game():
    print("Welcome to Number Guessing Game!")
    print("I am thinking of a number between 1 to  100")
    rand_num=randint(1, 100)
    turns=set_diff()

    ease_guess=0
    while rand_num!=ease_guess:
        print(f"You have {turns} attempts remaining to guess the number.")
        ease_guess=int(input("Make the guess: \n"))
        turns=comp_num(rand_num,ease_guess,turns)
        if turns==0:
            print("You've run out of guesses, you lose.")
            return

        elif rand_num != ease_guess:
            print("Guess again.")
stsrt_game()