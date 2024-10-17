from utils import quests
from utils import user_inputs

print ("Welcome to the POE speed-leveling guide!")
            
# calling the act function
act_input = user_inputs.get_valid_act()

# Act 1 decision making tree
# If the user is in Act 1, ask for the quest
if act_input == 1:
    print ("Here is the list of Act 1 quests:")
    for key, value in quests.act1.items():
        print (f"{key}: {value}")
        
    # calling the quest function
    quest_input = user_inputs.get_valid_quest_input(1, 11)
    
    # Check which quest the user selected and respond accordingly
    if quest_input == 4:
        print(f"{quests.act1[quest_input]} is optional quest, you can go on!")
        print ("Reward for the quest is Book of Regrets.")
    elif quest_input == 11:
        # calling the char_check function
        char_check = user_inputs.get_valid_char_check() # use the validated input
        if char_check == "yes" or char_check == "y":
            print ("You have to do it for the ascendancy!")
        else:
            print("You can skip it!")
    else:
        print(f"You have to do {quests.act1[quest_input]}.")
        
# Act 2 decision making tree
# If the user is in Act 2, ask for the quest
elif act_input == 2:
    print ("\nHere is the list of Act 2 quests:")
    for key, value in quests.act2.items():
        print (f"{key}: {value}")
        
    # calling the quest function
    quest_input = user_inputs.get_valid_quest_input(1, 14)
    
    if quest_input == 1 or quest_input == 2 or quest_input == 3:
        print (f"{quests.act2[quest_input]} is optional quest, you can go on!")
        # additional if/elif block for quest rewards
        if quest_input == 1:
            print ("Reward for the quest is Flask or Belt of your choice.")
        elif quest_input == 2:
            print ("Reward for the quest is unlocked Menagerie.")
        elif quest_input == 3:
            print ("Reward for the quest is whatever you managed to beastcraft.")
    
    elif quest_input == 14:
        # calling the char_check function
        char_check = user_inputs.get_valid_char_check()
        if char_check == "yes" or char_check == "y":
            print ("You have to do it for the ascendancy!")
        else:
            print ("You can skip it!")
    else:
        print (f"You have to do {quests.act2[quest_input]}.")
    
elif act_input == 3:
    pass

else:
    print("Act not implemented yet.")
    