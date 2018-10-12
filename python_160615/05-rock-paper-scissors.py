import random

try:
   raw_input
except NameError as ex:
   raw_input = input # python3
finally:
   pass

def beats(first, second):
    if (first, second) == ("paper", "rock"):
        return True
    if (first, second) == ("scissors", "paper"):
        return True
    if (first, second) == ("rock", "scissors"):
        return True
    return False

alternatives = ["rock", "paper", "scissors"]

computer_choice = random.choice(alternatives)

good_answer = False

while not good_answer:
    choices = ", ".join(alternatives)
    user_choice = raw_input("Make your choice ({0}): ".format(choices))
    if user_choice in alternatives:
        good_answer = True

print("I picked {}".format(computer_choice))

if beats(user_choice, computer_choice):
    print("You win")
elif beats(computer_choice, user_choice):
    print("I win")
else:
    print("It's a tie")
