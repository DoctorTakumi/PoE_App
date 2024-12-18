import tkinter as tk
# from tkinter import ttk  # Import ttk for the border line
from tkinter import messagebox
from utils import quests, quest_utils, quest_logic  # importing quest module


# Creating the main window
def create_gui():
    root = tk.Tk() # creates the main window for the application
    root.title("PoE Leveling App")  # title written on top of application
    # root.geometry ("400x300") # posibility to change GUI dimensions
    root.config(bg="lightgrey") # GUI background color
    

    # label and dropdown for act selection
    tk.Label(root, text="Which act are you in?", bg= "lightgrey", font=("Italic", 10, "bold")).grid(row=0, column=0, padx=10, pady=10) # label in GUI that prompts the user to select an act
    act_var = tk.StringVar()  # variable to hold selected act
    act_dropdown = tk.OptionMenu(root, act_var, *list(range(1, 11)))  # dropdown menu for acts 1 to 10
    act_dropdown.grid(row=0, column=1, padx=10, pady=10)  # places the dropdown in the grid layout at the specified row and column
    act_dropdown.config (bg = "#800020", fg = "white")  ## act button properties

    # label for quest selection (updated later based on act)
    quest_var = tk.StringVar()  # variable to hold selected quest
    tk.Label(root, text="Choose a quest:", bg= "lightgrey", font=("Italic", 10, "bold")).grid(row=1, column=0, padx=10, pady=10) # creates a label prompting the user to select a quest
    quest_dropdown = tk.OptionMenu(root, quest_var, "")  # creates an empty dropdown for quest selection
    quest_dropdown.grid(row=1, column=1, padx=10, pady=10)
    quest_dropdown.config (bg = "#800020", fg = "white")  ## quest button properties

    # updates the quest dropdown based on the selected act
    def update_quests(*args): # defines a function that updates the quest dropdown based on the act selected by the user
        act_input = int(act_var.get()) # retrieves the current value of the act selection dropdown and converts it to an integer
        quest_dropdown["menu"].delete(0, "end")  # clears any existing options in the quest dropdown before adding new ones
        if act_input == 1:
            for key, value in quests.act1.items():  # populating Act 1 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        elif act_input == 2:
            for key, value in quests.act2.items():  # populating Act 2 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        elif act_input == 3:
            for key, value in quests.act3.items():  # populating Act 3 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        elif act_input == 4:
            for key, value in quests.act4.items(): # populating Act 4 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        elif act_input == 5:
            for key, value in quests.act5.items(): # populating Act 5 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        elif act_input == 6:
            for key, value in quests.act6.items(): # populating Act 6 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        elif act_input == 7:
            for key, value in quests.act7.items(): # populating Act 7 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        elif act_input == 8:
            for key, value in quests.act8.items(): # populating Act 8 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        elif act_input == 9:
            for key, value in quests.act9.items(): # populating Act 9 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))
        elif act_input == 10:
            for key, value in quests.act10.items(): # populating Act 10 quests
                quest_dropdown["menu"].add_command(label=value, command=tk._setit(quest_var, value))

    # Trace act_var so that the quest list updates when act is selected
    # whenever its value changes (when a user selects an act), the update_quests function will be called automatically
    act_var.trace("w", update_quests)
    
    # adding a label to display the response (initially empty)!
    response_label = tk.Label(root, text="", bg = "lightgrey", fg="black", font=("Italic", 10, "bold"))  # label properties
    response_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    # Submit button functionality
    # defines the function that runs when the "Submit" button is clicked
    def submit():
        act = act_var.get() # retrieve the selected act
        quest = quest_var.get() # retrieve the selected quest

        # Check if act and quest are selected - if not, displays an error message
        if not act or not quest:
            messagebox.showerror("Error", "Please select both act and quest!")
            return

        act_input = int(act)  # convert the act to integer
        quest_input = quest_utils.get_quest_input(act_input, quest)  # calls the function from quest_utils to get the index of the selected quest

        # If quest_input is None, it means the quest selection is invalid, and an error message is displayed
        if quest_input is None:
            messagebox.showerror("Error", "Invalid quest selection!")
            return

        # Logic to determine the response based on selected quest
        # Based on the selected act, it calls the appropriate function from quest_logic to get the response related to the quest
        response = ""
        
        # Logic for selected quests - imported from quest_logic module
        if act_input == 1:
            response = quest_logic.handle_act_1_quests(quest_input)
        elif act_input == 2:
            response = quest_logic.handle_act_2_quests(quest_input)
        elif act_input == 3:
            response = quest_logic.handle_act_3_quests(quest_input)
        elif act_input == 4:
            response = quest_logic.handle_act_4_quests(quest_input)
        elif act_input == 5:
            response = quest_logic.handle_act_5_quests(quest_input)
        elif act_input == 6:
            response = quest_logic.handle_act_6_quests(quest_input)
        elif act_input == 7:
            response = quest_logic.handle_act_7_quests(quest_input)
        elif act_input == 8:
            response = quest_logic.handle_act_8_quests(quest_input)
        elif act_input == 9:
            response = quest_logic.handle_act_9_quests(quest_input)
        elif act_input == 10:
            response = quest_logic.handle_act_10_quests(quest_input)
            
        # Display the result to the user in a pop-up window
        ## messagebox.showinfo("Selected Quest", response) ## name of pop-up shit
        
        # updating the label with the response instead of a pop-up!!
        response_label.config(text=response)

    # submit button properties
    submit_button = tk.Button(root, text="Submit", bg = "#B58D3D", fg = "white", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    
    # starts the main loop of the application, which waits for user interaction and keeps the window open
    root.mainloop()

# Call the create_gui function to start the application
if __name__ == "__main__":
    create_gui()