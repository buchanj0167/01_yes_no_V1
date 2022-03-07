import random

# Functions go here

# checks user has entered an integer between low and high
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            #if the amount is too low / too high give
            if low < response <= high:
                return response
            
            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

# checks user has entered yes / no
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no") 


# prints nicely formatted instructions
def instructions():
    print()
    print("**** How to play ****")
    print("You will be asked how much you want to play with, "
          "type the amount you would like to play with, than click enter.")
    print()
    print("*** The rules of the game ***")
    print("When given an amount you want to play with it must be a number "
          "between 1-10.")
    print()
    return""

# makes the text look better, adds to the austhetics 
def statement_generator(statement, decoration, lines):

    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    
    if lines == 1:
        print(statement)
    else:
        top_bottom = decoration * len(statement)

        print(top_bottom)
        print(statement)
        print(top_bottom)

    return ""




# ******* Main Routine Goes here *******

# Greets the player  
greeting = "Welcome to the Lucky Unicorn Game"
sides = "*" * 3

greeting = "{} {} {}".format(sides, greeting, sides)

top_bottom = "*" * len(greeting)

print(top_bottom)
print(greeting)
print(top_bottom)

# Ask user if they have played before
show_instructions = yes_no("Would you like to see the instructions? ")

if show_instructions == "yes":
    instructions()



# Ask user how much they want to play with...
how_much = num_check("How much would you "
                     "like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1 

    # Print round number
    print()
    print("*** Rounds #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5, 
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4

    # if the random # is between 6 and 36
    # user get a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1

    # The token is either a horse or zebra...
    # in both cases, subtract $0.50 from the balance 
    else:
        # if the number is even, set th chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        # otherwise set it to a zebra    
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "You got a {}. Your balance is " \
              "${:.2f}".format(chosen, balance)
    
    statement_generator(outcome, prize_decoration, 1)

    if balance < 1 :
        # If balance is to low, exit the game and output a suitable message
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit ")

print()
print("Final balance $", balance)
print()
print("Final balance ${:.2f}".format(balance))
input()