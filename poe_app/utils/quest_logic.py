from utils import quests

# Logic for selected quests
# This is for adding more acts, quests and their rewards
def handle_act_1_quests(quest_input):
    response = ""
    if quest_input == 4:
        response += f"{quests.act1[quest_input]} is an optional quest, you can go on!\n"
        response += "Quest reward is Book of Regrets."
    elif quest_input == 11:
        response += "If this is your first character, you have to do it for the ascendancy!\n"
        response += "Otherwise, you can proceed!"
    else:
        response += f"You have to do {quests.act1[quest_input]}."
    return response

def handle_act_2_quests(quest_input):
    response = ""
    if quest_input in [1, 2, 3]:
        response += f"{quests.act2[quest_input]} is an optional quest, you can go on!\n"
        if quest_input == 1:
            response += "Quest reward is Flask or Belt of your choice."
        elif quest_input == 2:
            response += "Quest reward is unlocked Menagerie and Einhar unlocked in your Hideout."
        elif quest_input == 3:
            response += "Quest reward is whatever you managed to beastcraft."
    elif quest_input == 5:
        response += f"You have to do {quests.act2[quest_input]}.\n"
        response += "Quest is reworked and now grants 1 skill point."
    elif quest_input in [8, 9, 10, 11]:
        response += f"You have to do {quests.act2[quest_input]}.\n"
        if quest_input == 8:
            response += "Kill them all for 1 Passive Skill Point.\n"
            response += "Save Alira to get 15% to all Elemental Resistances.\n"
            response += "Save Kraitlyn to get 8% MS.\n"
            response += "Save Oak to get +40 to maximum life."
        elif quest_input == 9:
            response += "Save Alira to get 15% to all Elemental Resistances."
        elif quest_input == 10:
            response += "Save Kraitlyn to get 8% MS."
        elif quest_input == 11:
            response += "Save Oak to get +40 to maximum life."
    elif quest_input == 14:
        response += "If this is your first character, you have to do it for the ascendancy!\n"
        response += "Otherwise, you can proceed!"
    else:
        response += f"You have to do {quests.act2[quest_input]}."
    return response

def handle_act_3_quests(quest_input):
    response = ""
    if quest_input in [7, 8]:
        response += f"{quests.act3[quest_input]} is an optional quest, you can go on!\n"
        if quest_input == 7:
            response += "Quest reward is Coral/Gold/Paua Ring."
        elif quest_input == 8:
            response += "Quest reward is vast choice of Support gems.\n"
            response += "You also gain access to all the Support gems."
    elif quest_input == 3:
        response += "If this is your first character, you have to do it to finish the act!\n"
        response += "Otherwise, quest reward is vast choice of Skill gems."
    elif quest_input == 11:
        response += "If this is your first character, you have to do it for the ascendancy!\n"
        response += "Otherwise, you can proceed!"
    else:
        response += f"You have to do {quests.act3[quest_input]}."
    return response
        
def handle_act_4_quests(quest_input):
    response = ""
    if quest_input in [2, 3, 4]:
        response += f"{quests.act4[quest_input]} is an optional quest, you can go on!\n"
        if quest_input == 2:
            response += "Quest reward is access to the Azurite Mine and Niko unlocked in your Hideout.\n"
        elif quest_input == 3:
            response += "There is no quest reward.\n"
        elif quest_input == 4:
            response += "There is no quest reward.\n"
    else:
        response += f"You have to do {quests.act4[quest_input]}."
    return response

def handle_act_5_quests(quest_input):
    response = ""
    if quest_input == 5:
        response += f"{quests.act5[quest_input]} is an optional quest, you can go on!\n"
        response += "Quest reward is a weapon of your choice.\n"
    else:
        response += f"You have to do {quests.act5[quest_input]}."
    return response

def handle_act_6_quests(quest_input):
    response = ""
    if quest_input in [1, 2]:
        response += f"{quests.act6[quest_input]} is an optional quest, you can go on!\n"
        if quest_input == 1:
            response += "However, if this is your first character, you'll need it to unlock Lilly in your Hideout!\n"
            response += "Otherwise, quest reward is Book of Regrets and vast choice of Skill/Support gems"
        elif quest_input == 2:
            response += "Quest reward is Amulet or Belt of your choice."
    else:
        response += f"You have to do {quests.act6[quest_input]}."
    return response

def handle_act_7_quests(quest_input):
    response = ""
    if quest_input in [1, 3, 6]:
        response += f"{quests.act7[quest_input]} is an optional quest, you can go on!\n"
        if quest_input == 1:
            response += "Quest reward is Utility Flask of your choice."
        elif quest_input == 3:
            response += "Quest reward is Alva unlocked in your Hideout.\n"
        elif quest_input == 6:
            response += "Quest reward is Amulet of your choice."
    else:
        response += f"You have to do {quests.act7[quest_input]}."
    return response

def handle_act_8_quests(quest_input):
    response = ""
    if quest_input == 5:
        response += f"{quests.act8[quest_input]} is an optional quest, you can go on!\n"
        response += "Quest reward is Jewel of your choice."
    else:
        response += f"You have to do {quests.act8[quest_input]}."
    return response

def handle_act_9_quests(quest_input):
    response = ""
    if quest_input in [1, 3]:
        response += f"{quests.act9[quest_input]} is an optional quest, you can go on!\n"
        if quest_input == 1:
            response += "Quest reward is Jun unlocked in your Hideout.\n"
        elif quest_input == 3:
            response += "Quest reward is Book of Regrets."
    else:
        response += f"You have to do {quests.act9[quest_input]}."
    return response

def handle_act_10_quests(quest_input):
    response = ""
    if quest_input in [2, 3]:
        response += f"{quests.act10[quest_input]} is an optional quest, you can go on!\n"
        if quest_input == 2:
            response += "Quest reward is Belt of your choice."
        elif quest_input == 3:
            response += "Quest reward is Book of Regrets."
    else:
        response += f"You have to do {quests.act10[quest_input]}."
    return response