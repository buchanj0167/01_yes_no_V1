print("Hello, Welcome to my game")

#Ask the user if they have played before
show_instructions = input("have you played this game before?").lower()
                      
#If they say yes, output 'program continues'
if show_instructions == "yes":
    print("program continues")

elif show_instructions == "y":
    print("program continues")

elif show_instructions == "no":
    print("display instructions")

elif show_instructions == "n":
    print("**** How to play ****")
    print()
    print("The rules of the game go here")


#If they say no, output 'display instructions'
else:
     print("Please answer yes / no")


# Main routine go here

error = "Please enter an whole number between 1 and 10\n"

valid = False
while not valid:
        try:
            #ask the question
            response = int(input("How much would you"
                                "like to play with? "))
            #if the amount is too low / too high give
            if 0 < response <= 10:
                print("You have asked to play"
                    "with ${}".format(response))

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

