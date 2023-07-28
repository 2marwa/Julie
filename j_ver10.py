########################################################################
###  This program is so julie can track items hired from her store   ###
########################################################################

#import tkinter so i can use GUI
from tkinter import *
import random
#quit subroutine
def quit():
    main_window.destroy()

#print details of all the items
def print_hire_details():
    # Clear all the labels before printing
    for widget in main_window.winfo_children():
        grid_info = widget.grid_info()
        if grid_info and grid_info['row'] >= 8:
            widget.grid_remove()
# Create the column headings for "Print Details"
    Label(main_window, font=("Helvetica 10 bold"), text="Row").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Item Hired").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="No. Items Hired").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Receipt No.").grid(column=4, row=7)
    #add each item in the list into its own row
    for name_count, details in enumerate(hire_details):
        Label(main_window, text=name_count).grid(column=0, row=name_count + 8)
        Label(main_window, text=details[0]).grid(column=1, row=name_count + 8)
        Label(main_window, text=details[1]).grid(column=2, row=name_count + 8)
        Label(main_window, text=details[2]).grid(column=3, row=name_count + 8)
        Label(main_window, text=details[3]).grid(column=4, row=name_count + 8)
        
#Check the inputs are all valid
def check_inputs ():
    input_check = 0
    Label(main_window, text="               ") .grid(column=2,row=0)
    Label(main_window, text="               ") .grid(column=2,row=1)
    Label(main_window, text="               ") .grid(column=2,row=2)
    Label(main_window, text="               ") .grid(column=2,row=3)

    #Check that Name is not blank, set error text if blank   
    if len(entry_name.get()) == 0:
        Label(main_window,fg="red", text="Required") .grid(column=2,row=0)
        input_check = 1
     
    #Check that Item Hired is not blank, set error text if blank     
    if len(entry_item.get()) == 0 :
        Label(main_window,fg="red", text="Required") .grid(column=2,row=1)
        input_check = 1
    #Check the Number of Items is not blank and between 1 and 500, set error text if blank  
    if (entry_hires.get().isdigit()) : 
        if  int(entry_hires.get()) < 1 or  int(entry_hires.get()) > 500:
            Label(main_window,fg="red", text="1-500 only") .grid(column=2,row=2)
            input_check = 1
    else :
        Label(main_window,fg="red", text="1-500 only") .grid(column=2,row=2)
        input_check = 1

    if input_check == 0 : append_name() 

        
            
#add the next item to the list
def append_name ():
    #append each item to its own area of the list
    random_receipt = random.randint(1000000, 9999999)
    hire_details.append([entry_name.get(), entry_item.get(), entry_hires.get(), random_receipt])
    entry_name.delete(0,'end')
    entry_item.delete(0,'end')
    entry_hires.delete(0,'end')
    counters['total_entries'] += 1

def delete_row():
    # Get the row number to delete
    row_to_delete = int(delete_item.get())

    # Check if the row number is within the valid range of entries
    if 0 <= row_to_delete < len(hire_details):
        # Remove the row from hire_details
        del hire_details[row_to_delete]
        counters['total_entries'] -= 1
        # Clear the input box for the row number
        delete_item.delete(0, 'end')
        # Print the updated hire details
        print_hire_details()
    else:
        # If the row number is invalid, display an error message (optional)
        Label(main_window, fg="red", text="Invalid Row").grid(column=4, row=3)

#create the buttons and labels
def setup_buttons():
    #create all the empty and default labels, buttons and entry boxes. Put them in the correct grid position
    Label(main_window, text="Name") .grid(column=0,row=0,sticky=E)
    Label(main_window, text="Item") .grid(column=0,row=1,sticky=E)
    Button(main_window, text="Quit",command=quit,width = 10, bg="#dca2de") .grid(column=4, row=0,sticky=E)
    Button(main_window, text="Append Details",command=check_inputs, bg="#dca2de") .grid(column=3,row=1)
    Button(main_window, text="Print Details", command=print_hire_details, width=10,bg="#dca2de").grid(column=4, row=1, sticky=E)
    Label(main_window, text="No of Items") .grid(column=0,row=2,sticky=E)
    Label(main_window, text="Row #") .grid(column=3,row=2,sticky=E)
    Button(main_window, text="Delete Row",command=delete_row,width = 10,bg="#dca2de") .grid(column=4,row=3,sticky=E)
    Label(main_window, text="               ") .grid(column=2,row=0)
    Label(main_window, text=" ").grid(column=2, row=0)  # So the layout is will not be disrupted by the colour




#start the program running
def main():
    #Start the GUI it up
    setup_buttons()
    main_window.configure(bg="#f6d0f7")
    main_window.mainloop()
    
#create empty list for hire details and empty variable for entries in the list
counters = {'total_entries': 0, 'name_count': 0}
hire_details = []
main_window = Tk()
entry_name = Entry(main_window)
entry_name.grid(column=1, row=0)
entry_item = Entry(main_window)
entry_item.grid(column=1, row=1)
entry_hires = Entry(main_window)
entry_hires.grid(column=1, row=2)
delete_item = Entry(main_window)
delete_item.grid(column=3, row=3)
main()

