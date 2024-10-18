from utils import quests

# Logic for selected quests
# This is for adding more acts, quests and their rewards
def handle_act_1_quests(quest_input):
    response = ""
    if quest_input == 4:
        response += f"{quests.act1[quest_input]} is an optional quest, you can go on!\n"
        response += "Reward for the quest is Book of Regrets."
    elif quest_input == 11:
        response += "If this is your first character, you have to do it for the ascendancy!\n"
        response += "Otherwise, you can proceed!"
    else:
        response += f"You have to do {quests.act1[quest_input]}."
    return response

def handle_act_2_quests(quest_input):
    response = ""
    if quest_input in [1, 2, 3]:
        response += f"{quests.act2[quest_input]} is an optional quest, you can go on!"
        if quest_input == 1:
            response += " Reward for the quest is Flask or Belt of your choice."
        elif quest_input == 2:
            response += " Reward for the quest is unlocked Menagerie."
        elif quest_input == 3:
            response += " Reward for the quest is whatever you managed to beastcraft."
    elif quest_input == 5:
        response += f"You have to do {quests.act2[quest_input]}.\n"
        response += "Quest is reworked and now grants 1 skill point."
    elif quest_input in [9, 10, 11]:
        response += f"You have to do {quests.act2[quest_input]}.\n"
        if quest_input == 9:
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

