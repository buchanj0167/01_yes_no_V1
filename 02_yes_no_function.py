#Functions go here...

# Checks that user response is yes / no
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
   

#Main routine goes here...
show_instructions = yes_no("have you played this game before ")

print("you chose {}".format(show_instructions))

