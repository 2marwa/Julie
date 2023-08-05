
from tkinter import * # So I can use GUI
import random # For the receipt number
from tkinter import messagebox


def quit():
    main_window.destroy() #For quit button to end to programme, regardless of progress

def error_window(message):
    messagebox.showerror("Error", message)

def print_hire_details():
    for widget in main_window.winfo_children():
        grid_info = widget.grid_info()
        if grid_info and grid_info['row'] >= 10:
            widget.grid_remove()

    headings = ["Row", "Name", "Item Hired", "No. Items Hired", "Receipt No."] # Create headings for the "Print Details"
    for col, heading in enumerate(headings):
        Label(main_window, text=heading, font=("Helvetica 10"), relief=RIDGE, padx=10, pady=5).grid(column=col, row=10)

    for row, details in enumerate(hire_details):
        # Add row number (starting from 0) to the beginning of the details list
        details_with_row_number = [row] + details
        for col, value in enumerate(details_with_row_number, start=0):
            Label(main_window, text=value, relief=RIDGE, padx=10, pady=5).grid(column=col, row=row + 11)  

def check_inputs():
    name = entry_name.get()
    amount_hired = entry_hires.get()

    if not name or not name.isalpha():
        error_window("Please enter your name using letters a-z!")
        return
    if not amount_hired.isdigit() or int(amount_hired) > 500 or int(amount_hired) < 1:
        error_window("Please enter 1-500!")
        return

    save_details()

def save_details():
    random_receipt = random.randint(1000000, 9999999) # Generate random number between 1000000 and 9999999
    hire_details.append([entry_name.get(), item_var.get(), entry_hires.get(), random_receipt]) # Making sure the information is printed in the right columns 
    entry_name.delete(0, 'end')
    entry_hires.delete(0, 'end')
    counters['total_entries'] += 1

def delete_row():
    input_text = delete_item.get().strip()  # Remove leading and trailing whitespace

    if not input_text:
        error_window("Please enter the row number first.\n You can use the 'Print Details' button to find the row number!")
        return

    try:
        row_to_delete = int(input_text)
    except ValueError:
        error_window("Please enter the row number first.\n You can use the 'Print Details' button to find the row number!")
        return
    
    if 0 <= row_to_delete < len(hire_details):
        del hire_details[row_to_delete]
        counters['total_entries'] -= 1
        delete_item.delete(0, 'end')
        print_hire_details()  # Display updated Hire Details (without needing to press 'print details' again)
    else:
        error_window("Please enter an existing row number!")

def setup_buttons(): # Set up the buttons and their positions on the GUI
    Label(main_window, text="Name").grid(column=0, row=0, sticky=E, padx=10, pady=5)
    Label(main_window, text="Item").grid(column=0, row=1, sticky=E, padx=10, pady=5)
    Button(main_window, text="Quit", command=quit, width=10, bg="#dca2de").grid(column=6, row=7, sticky=E, padx=10, pady=5)
    Button(main_window, text="Save Details", command=check_inputs, bg="#dca2de").grid(column=0, row=7, padx=10, pady=5)
    item_dropdown.config(bg="#dca2de")  # Set the background color of the dropdown menu in dark pink
    Button(main_window, text="Print Details", command=print_hire_details, width=10, bg="#dca2de").grid(column=6, row=0, sticky=E, padx=10, pady=5)
    Label(main_window, text="No of Items").grid(column=0, row=2, sticky=E, padx=10, pady=5)
    Label(main_window, text="Row #").grid(column=4, row=3, sticky=E, padx=10, pady=5)
    Button(main_window, text="Delete Row", command=delete_row, width=10, bg="#dca2de").grid(column=6, row=3, sticky=E, padx=10, pady=5)

def main():
    setup_buttons()
    main_window.configure(bg="#f6d0f7")
    main_window.mainloop()

counters = {'total_entries': 0, 'name_count': 0}
hire_details = []

main_window = Tk()
main_window.title("Julie's Hire Store Tracker")

# Add a border around the main window
main_window.configure(borderwidth=10, relief='ridge')

entry_name = Entry(main_window)
entry_name.grid(column=1, row=0, padx=7, pady=5)

# List of items to be offered in the dropdown menu
items = ["Balloon", "Bluetooth Speaker", "Party Hat", "Candles - Multipack", "Confetti Cannon"]
item_var = StringVar(main_window)
item_var.set(items[0])  # Set the default value to the first item in the list
item_dropdown = OptionMenu(main_window, item_var, *items)
item_dropdown.grid(column=1, row=1, padx=10, pady=5)
entry_hires = Entry(main_window)
entry_hires.grid(column=1, row=2, padx=10, pady=5)
delete_item = Entry(main_window)
delete_item.grid(column=5, row=3, padx=10, pady=5)

main()

