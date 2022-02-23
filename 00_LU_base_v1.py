print("Hello, Welcome to my game")

#Ask the user if they have played before
show_instructions = input("have you played this game before?").lower()
                      
#Functions go here...
def yes_no(question):
    valid = False
    while not valid:
           response = input(question).lower()
    
    if response == "yes" or response == "y":
        response = "yes"
        return response

    elif response == "no" or response == "n":
        response = "no"
        return response

    else:
        print("Please answer yes / no")
   


#Main routine goes here...
show_instructions = yes_no("have you played this game before")

print("you chose {}".format(show_instructions))


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