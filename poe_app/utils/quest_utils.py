from utils import quests

# Function to get quest input based on the act and quest string
# To add acts and match them with dictionary from quest module
def get_quest_input(act_input, quest):
    if act_input == 1:
        # Get the index for Act 1 quests
        try:
            quest_index = list(quests.act1.values()).index(quest) + 1  # +1 to match the dictionary keys
            return quest_index
        except ValueError:
            return None  # Quest not found
    elif act_input == 2:
        # Get the index for Act 2 quests
        try:
            quest_index = list(quests.act2.values()).index(quest) + 1
            return quest_index
        except ValueError:
            return None  # Quest not found
    elif act_input == 3:
        try:
            quest_index = list(quests.act3.values()).index(quest) + 1
            return quest_index
        except ValueError:
            return None
    elif act_input == 4:
        try:
            quest_index = list(quests.act4.values()).index(quest) + 1
            return quest_index
        except:
            return None
    elif act_input == 5:
        try:
            quest_index = list(quests.act5.values()).index(quest) + 1
            return quest_index
        except:
            return None
    return None  # Act not implemented