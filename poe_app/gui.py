import tkinter as tk
from tkinter import messagebox
from utils import quests, quest_utils, quest_logic  # importing quest module


# Creating the main window
def create_gui():
    root = tk.Tk()
    root.title("PoE Leveling App")  # name written on top of GUI

    # label and dropdown for act selection
    tk.Label(root, text="Which act are you in?").grid(row=0, column=0, padx=10, pady=10)
    act_var = tk.StringVar()  # variable to hold selected act
    act_dropdown = tk.OptionMenu(root, act_var, *list(range(1, 11)))  # acts 1 to 10
    act_dropdown.grid(row=0, column=1, padx=10, pady=10)  # dimensions of the Act dropdown

    # label for quest selection (updated later based on act)
    quest_var = tk.StringVar()  # variable to hold selected quest
    tk.Label(root, text="Choose a quest: ").grid(row=1, column=0, padx=10, pady=10)
    quest_dropdown = tk.OptionMenu(root, quest_var, "")  # start with empty
    quest_dropdown.grid(row=1, column=1, padx=10, pady=10)

    # updates the quest dropdown based on the selected act
    def update_quests(*args):
        act_input = int(act_var.get())
        quest_dropdown["menu"].delete(0, "end")  # clear existing options
        if act_input == 1:
            for key, value in quests.act1.items():  # populating Act 1 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        elif act_input == 2:
            for key, value in quests.act2.items():  # populating Act 2 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))

    # Trace act_var so that the quest list updates when act is selected
    act_var.trace("w", update_quests)

    # Submit button functionality
    def submit():
        act = act_var.get()
        quest = quest_var.get()

        # Check if act and quest are selected
        if not act or not quest:
            messagebox.showerror("Error", "Please select both act and quest!")
            return

        act_input = int(act)  # convert the act to integer
        quest_input = quest_utils.get_quest_input(act_input, quest)  # call get_quest_input

        if quest_input is None:
            messagebox.showerror("Error", "Invalid quest selection!")
            return

        # Logic to determine the response based on selected quest
        response = ""
        
        # Logic for selected quests - imported from quest_logic module
        if act_input == 1:
            response = quest_logic.handle_act_1_quests(quest_input)
        elif act_input == 2:
            response = quest_logic.handle_act_2_quests(quest_input)
            
        # Display the result to the user
        messagebox.showinfo("Selected Quest", response) ## name of pop-up shit

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

# Call the create_gui function to start the application
if __name__ == "__main__":
    create_gui()