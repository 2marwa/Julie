
from tkinter import * # So I can use GUI.
import random # For the receipt number.
from tkinter import messagebox # For error windows.


def quit():
    main_window.destroy() # For the quit button to end to programme, regardless of progress.

def error_window(message):
    messagebox.showerror("Error", message) # Create pop up message.

def print_hire_details():
    for widget in main_window.winfo_children():
        grid_info = widget.grid_info()
        if grid_info and grid_info['row'] >= 10:
            widget.grid_remove() # if a widget is placed in a row with an index of 10 or higher, it will be hidden so the GUI willbe kept neat.

    headings = ["Row", "Name", "Item Hired", "No. Items Hired", "Receipt No."] # Create headings for the "Print Details"
    for col, heading in enumerate(headings): # To apply the appearence details to all headings at once
        Label(main_window, text=heading, font=("Helvetica 10"), relief=RIDGE, padx=10, pady=5).grid(column=col, row=10) #Picking font and font size.

    for row, details in enumerate(hire_details):
        # Add row number (starting from 0) to the beginning of the details list.
        details_with_row_number = [row] + details # How to display information from inout under the heaidngs.
        for col, value in enumerate(details_with_row_number, start=0): # Creating new list
            Label(main_window, text=value, relief=RIDGE, padx=10, pady=5).grid(column=col, row=row + 11) # Choosing how it should display (style, grid placement)

def check_inputs():
    name = entry_name.get() # Retriving the user's name.
    amount_hired = entry_hires.get() # Retriving the amount of the item the user has hired.

    if not name or not name.isalpha(): # If the name is not a-z, display error window.
        error_window("Please enter your name using letters a-z!") # Clarifying what the error window will say.
        return # Continuing.
    if not amount_hired.isdigit() or int(amount_hired) > 500 or int(amount_hired) < 1: # If amount hired isn't a digit between 1-500, display error window.
        error_window("Please enter 1-500!")# Clarifying what the error window will say.
        return # Continue.

    save_details() # Once input is correct, save the details.

def save_details():
    random_receipt = random.randint(1000000, 9999999) # Generate random number between 1000000 and 9999999.
    hire_details.append([entry_name.get(), item_var.get(), entry_hires.get(), random_receipt]) # Making sure the information is printed in the right columns.
    entry_name.delete(0, 'end') # Clear the input once the input is correct (no errors) and saved .
    entry_hires.delete(0, 'end') # Clear the input once the input is correct (no errors) and saved.
    counters['total_entries'] += 1 # Tracking row number (adding 1 to all new 'entries').

def delete_row():
    input_text = delete_item.get().strip() # Remove whitespace.

    if not input_text: # If the Delete row button is pressed without text, display error window.
        error_window("Please enter the row number first.\n You can use the 'Print Details' button to find the row number!") # CLarifying what the error window will say.
        return # Continue.

    try:
        row_to_delete = int(input_text)
    except ValueError: # Removing value error possibility so nothing will print in the shell.
        error_window("Please enter the row number first.\n You can use the 'Print Details' button to find the row number!") # Clarifying what the error window will say.
        return #Continue.
    
    if 0 <= row_to_delete < len(hire_details): # Making sure the number is in a valid range.
        del hire_details[row_to_delete]
        counters['total_entries'] -= 1 # Remove 1 from the row count (automatically renumbers row so there isn't a number missing).
        delete_item.delete(0, 'end') # Clear the row number inputted into the box after the row has been deleted.
        print_hire_details()  # Display updated Hire Details (without needing to press 'print details' again).
    else:
        error_window("Please enter an existing row number!")

def setup_buttons(): # Set up the buttons and their positions on the GUI
    Label(main_window, text="Name").grid(column=0, row=0, sticky=E, padx=10, pady=5) # Putting the Label into correct position in grid.
    Label(main_window, text="Item").grid(column=0, row=1, sticky=E, padx=10, pady=5) # Putting the Label into correct position in grid.
    Button(main_window, text="Quit", command=quit, width=10, bg="#dca2de").grid(column=6, row=7, sticky=E, padx=10, pady=5)# Putting the Button into correct position in grid.
    Button(main_window, text="Save Details", command=check_inputs, bg="#dca2de").grid(column=0, row=7, padx=10, pady=5) # Putting the Button into correct position in grid.
    item_dropdown.config(bg="#dca2de")  # Setting the background color of the dropdown menu to dark pink (to match the other buttons).
    Button(main_window, text="Print Details", command=print_hire_details, width=10, bg="#dca2de").grid(column=6, row=0, sticky=E, padx=10, pady=5) # Putting the Button into correct position in grid.
    Label(main_window, text="No of Items").grid(column=0, row=2, sticky=E, padx=10, pady=5) # Putting the Label into correct position in grid.
    Label(main_window, text="Row #").grid(column=4, row=3, sticky=E, padx=10, pady=5) # Putting the Label into correct position in grid.
    Button(main_window, text="Delete Row", command=delete_row, width=10, bg="#dca2de").grid(column=6, row=3, sticky=E, padx=10, pady=5) # Putting the Buttons into correct position in grid.

def main():
    setup_buttons()
    main_window.configure(bg="#f6d0f7") # Setting background colout to light pink.
    main_window.mainloop() # Starts the GUI loop.

counters = {'total_entries': 0, 'name_count': 0} # Setting counter to 0.
hire_details = [] # Creating an empty list to add information to.

main_window = Tk() # Allows the main window to run in/with Tk.
main_window.title("Julie's Hire Store Tracker") # Setting what the window will display as a title.

main_window.configure(borderwidth=10, relief='ridge') # Adding a border around the main window.entry_name = Entry(main_window).
entry_name.grid(column=1, row=0, padx=7, pady=5) # Setting where the input box will be.

# List of items to be offered in the dropdown menu
items = ["Balloon", "Bluetooth Speaker", "Party Hat", "Candles - Multipack", "Confetti Cannon"]
item_var = StringVar(main_window)
item_var.set(items[0])  # Set the default value to the first item in the list.
item_dropdown = OptionMenu(main_window, item_var, *items)
item_dropdown.grid(column=1, row=1, padx=10, pady=5) # Setting where the dropdown menu box will be.

entry_hires = Entry(main_window)
entry_hires.grid(column=1, row=2, padx=10, pady=5) # Setting where the input box will be.
delete_item = Entry(main_window)
delete_item.grid(column=5, row=3, padx=10, pady=5) # Setting where the input box will be.

main()

