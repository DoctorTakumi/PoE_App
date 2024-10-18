import tkinter as tk
from tkinter import ttk, messagebox  # importing messagebox (.showinfo, .showerror)
from utils import quests  # importing quest module

# Function to get quest input based on the act and quest string
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
    return None  # Act not implemented


# Creating the main window
def create_gui():
    root = tk.Tk()
    root.title("PoE Leveling App")  # name written on top of GUI

    # label and dropdown for act selection
    tk.Label(root, text="Which act are you in?").grid(row=0, column=0, padx=10, pady=10)  # location of the question
    act_var = tk.StringVar()  # variable to hold selected act
    act_dropdown = tk.OptionMenu(root, act_var, *list(range(1, 11)))  # acts 1 to 10
    act_dropdown.grid(row=0, column=1, padx=10, pady=10)  # dimensions of the Act dropdown

    # label for quest selection (updated later based on act)
    quest_var = tk.StringVar()  # variable to hold selected quest
    quest_label = tk.Label(root, text="Choose a quest: ").grid(row=1, column=0, padx=10, pady=10)
    quest_dropdown = tk.OptionMenu(root, quest_var, "")  # start with empty
    quest_dropdown.grid(row=1, column=1, padx=10, pady=10)

    # updates the quest dropdown based on the selected act
    def update_quests(*args):
        act_input = int(act_var.get())
        quest_dropdown["menu"].delete(0, "end")  # added to clear existing options
        if act_input == 1:
            for key, value in quests.act1.items():  # populating Act 1 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        elif act_input == 2:
            for key, value in quests.act2.items():  # populating Act 2 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        # add more act when they are done!

    # Trace act_var so that the quest list updates when act is selected
    act_var.trace("w", update_quests)

    # Submit button functionality
    # handles user input and display appropriate quest response based on the selections made
    def submit():
        act = act_var.get()
        quest = quest_var.get()

        # Check if act and quest are selected
        if not act or not quest:
            messagebox.showerror("Error", "Please select both act and quest!")
            return

        act_input = int(act)  # convert the act to integer
        quest_input = get_quest_input(act_input, quest)

        if quest_input is None:
            messagebox.showerror("Error", "Invalid quest selection!")
            return

        # Logic to determine the response based on selected quest
        response = ""

        # Logic for selected quests!
        if act_input == 1:
            if quest_input == 4:
                response += f"{quests.act1[quest_input]} is an optional quest, you can go on!\n"
                response += "Reward for the quest is Book of Regrets."
            elif quest_input == 11:
                response += "If this is your first character, you have to do it for the ascendancy!\n"
                response += "Otherwise, you don't have to do it."
            else:
                response += f"You have to do {quests.act1[quest_input]}."

        elif act_input == 2:
            if quest_input in [1, 2, 3]:
                response += f"{quests.act2[quest_input]} is an optional quest, you can go on!"
                # Additional if/elif block for quest rewards
                if quest_input == 1:
                    response += " Reward for the quest is Flask or Belt of your choice."
                elif quest_input == 2:
                    response += " Reward for the quest is unlocked Menagerie."
                elif quest_input == 3:
                    response += " Reward for the quest is whatever you managed to beastcraft."
            elif quest_input == 14:
                response += "If this is your first character, you have to do it for the ascendancy!\n"
                response += "Otherwise, you don't have to do it."
            else:
                response += f"You have to do {quests.act2[quest_input]}."

        # Display the result to the user
        messagebox.showinfo("Selected Quest", response)

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()
