########################################################################
###  This program is so julie can track items hired from her store   ###
########################################################################

#import tkinter so i can use GUI
from tkinter import *

#quit subroutine
def quit():
    main_window.destroy()

#print details of all the items
def print_hire_details ():
    name_count = 0
    #Create the column headings for "Print Details"
    Label(main_window, font=("Helvetica 10 bold"),text="Row").grid(column=0,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Name").grid(column=1,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Item Hired").grid(column=2,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="No. Items Hired").grid(column=3,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Receipt No.").grid(column=4,row=7)

    #add each item in the list into its own row
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
    #Check that Name is not blank, set error text if blank   
    if len(entry_name.get()) == 0 :
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
    hire_details.append([entry_name.get(),entry_item.get(),entry_hires.get()])
    #clear the boxes
    entry_name.delete(0,'end')
    entry_item.delete(0,'end')
    entry_hires.delete(0,'end')
    counters['total_entries'] += 1

#delete a row from the list
def delete_row ():
    #find which row is to be deleted and delete it
    del hire_details[int(delete_item.get())]
    counters['total_entries'] -= 1
    name_count = counters['name_count']
    delete_item.delete(0,'end')
    #clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0,row=name_count+7) 
    Label(main_window, text="       ").grid(column=1,row=name_count+7)
    Label(main_window, text="       ").grid(column=2,row=name_count+7)
    Label(main_window, text="       ").grid(column=3,row=name_count+7)
    Label(main_window, text="       ").grid(column=4,row=name_count+7)
    #print all the items in the list
    print_hire_details()

