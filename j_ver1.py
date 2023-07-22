from tkinter import *

def quit():
    main_window.destroy()

#print details
def print_hire_details ():
    name_count = 0
    #Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),text="Row").grid(column=0,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Name").grid(column=1,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Item Hired").grid(column=2,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="No. Items Hired").grid(column=3,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Receipt No.").grid(column=4,row=7)

    #add each item in the list 
    while name_count < counters['total_entries'] :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        Label(main_window, text=(hire_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(main_window, text=(hire_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(hire_details[name_count][2])).grid(column=3,row=name_count+8)
        name_count +=  1
        counters['name_count'] = name_count
        
#Check the inputs are all valid
def check_inputs ():
    input_check = 0
    Label(main_window, text="               ") .grid(column=2,row=0)
    Label(main_window, text="               ") .grid(column=2,row=1)
    Label(main_window, text="               ") .grid(column=2,row=2)
    Label(main_window, text="               ") .grid(column=2,row=3)
    #Check that Name is not blank 
    if len(entry_name.get()) == 0 :
        Label(main_window,fg="red", text="Required") .grid(column=2,row=0)
        input_check = 1
