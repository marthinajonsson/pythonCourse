import random

try:
   raw_input
except NameError as ex:
   raw_input = input # python3
finally:
   pass

LOWER_LIMIT = 100
UPPER_LIMIT = 999

print("I'm thinking of a number between {0} and {1}.".format(LOWER_LIMIT, UPPER_LIMIT))

goal = random.randint(LOWER_LIMIT, UPPER_LIMIT)
guessed_it_yet = False
attempts = 0

while not guessed_it_yet:
    print()
    guess = int(raw_input("Make a guess: "))
    attempts += 1

    if guess > goal:
        print("Your guess was too high. Go lower.")
    elif guess < goal:
        print("Your guess was too low. Go higher.")
    else:
        guessed_it_yet = True

print("Yes, you got it! It was {0}.".format(goal))
print("It took you {0} guesses.".format(attempts))