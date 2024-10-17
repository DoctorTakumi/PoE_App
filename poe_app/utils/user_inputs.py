# Get input for the act
# Function to validate act input
def get_valid_act():
    while True:
        try:
            act_input = int(input("Which act are you in?: "))
            if act_input >= 1 and act_input <=10:
                return act_input
            else:
                print ("Invalid input! Please enter a number between 1 and 10!")
        except ValueError:
            print ("Invalid input! Please enter a valid number between 1 and 10!")

# function to validate quest input with dynamic range
def get_valid_quest_input(min_quest, max_quest):
        while True:
            try:
                quest_input = int(input(f"\nWhich quest are you on? (Enter number {min_quest}-{max_quest}): "))
                if quest_input >= min_quest and quest_input <= max_quest:
                    return quest_input
                else:
                    print (f"Invalid input! Please enter a number between {min_quest} and {max_quest}!")
            except ValueError:
                print (f"Invalid input! Please enter a valid number between {min_quest} and {max_quest}!")
                
# function to validate yes/no input
def get_valid_char_check():
    while True:
        char_check = input("Is this your first character?: ").lower()
        if char_check in ["yes", "y", "no", "n"]: ## the only accepted user answers
            return char_check
        else:
            print("Invalid input! Enter yes/no or y/n!")