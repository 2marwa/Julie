from tkinter import *
import random

def quit():
    main_window.destroy()

def print_hire_details():
    for widget in main_window.winfo_children():
        grid_info = widget.grid_info()
        if grid_info and grid_info['row'] >= 8:
            widget.grid_remove()

    headings = ["Row", "Name", "Item Hired", "No. Items Hired", "Receipt No."]
    for col, heading in enumerate(headings):
        Label(main_window, font=("Helvetica 10 bold"), text=heading, relief=RAISED, padx=10, pady=5).grid(column=col, row=7)

    for row, details in enumerate(hire_details):
        # Add row number (starting from 0) to the beginning of the details list
        details_with_row_number = [row] + details
        for col, value in enumerate(details_with_row_number, start=0):
            Label(main_window, text=value, relief=RIDGE, padx=10, pady=5).grid(column=col, row=row + 8)

def check_inputs():
    input_check = 0
    input_labels = [Label(main_window, text="               ") for _ in range(4)]
    input_labels[0].grid(column=2, row=0)
    input_labels[1].grid(column=2, row=1)
    input_labels[2].grid(column=2, row=2)
    input_labels[3].grid(column=2, row=3)

    if len(entry_name.get()) == 0:
        input_labels[0].configure(fg="red", text="Required")
        input_check = 1
     
    if len(entry_item.get()) == 0:
        input_labels[1].configure(fg="red", text="Required")
        input_check = 1

    if not entry_hires.get().isdigit() or int(entry_hires.get()) < 1 or int(entry_hires.get()) > 500:
        input_labels[2].configure(fg="red", text="1-500 only")
        input_check = 1

    if input_check == 0:
        append_name()

def append_name():
    random_receipt = random.randint(1000000, 9999999)
    hire_details.append([entry_name.get(), entry_item.get(), entry_hires.get(), random_receipt])
    entry_name.delete(0, 'end')
    entry_item.delete(0, 'end')
    entry_hires.delete(0, 'end')
    counters['total_entries'] += 1

def delete_row():
    row_to_delete = int(delete_item.get())
    if 0 <= row_to_delete < len(hire_details):
        del hire_details[row_to_delete]
        counters['total_entries'] -= 1
        delete_item.delete(0, 'end')
        print_hire_details()
    else:
        Label(main_window, fg="red", text="Invalid Row").grid(column=4, row=3)

def setup_buttons():
    Label(main_window, text="Name").grid(column=0, row=0, sticky=E, padx=10, pady=5)
    Label(main_window, text="Item").grid(column=0, row=1, sticky=E, padx=10, pady=5)
    Button(main_window, text="Quit", command=quit, width=10, bg="#dca2de").grid(column=4, row=0, sticky=E, padx=10, pady=5)
    Button(main_window, text="Append Details", command=check_inputs, bg="#dca2de").grid(column=4, row=2, padx=10, pady=5)
    Button(main_window, text="Print Details", command=print_hire_details, width=10, bg="#dca2de").grid(column=4, row=1, sticky=E, padx=10, pady=5)
    Label(main_window, text="No of Items").grid(column=0, row=2, sticky=E, padx=10, pady=5)
    Label(main_window, text="Row #").grid(column=3, row=2, sticky=E, padx=10, pady=5)
    Button(main_window, text="Delete Row", command=delete_row, width=10, bg="#dca2de").grid(column=4, row=3, sticky=E, padx=10, pady=5)
    Label(main_window, text="               ").grid(column=2, row=0)
    Label(main_window, text=" ").grid(column=2, row=0)  # So the layout will not be disrupted by the color

def main():
    setup_buttons()
    main_window.configure(bg="#f6d0f7")
    main_window.mainloop()

counters = {'total_entries': 0, 'name_count': 0}
hire_details = []

main_window = Tk()
main_window.title("Julie's Hire Store Tracker")
main_window.geometry("600x400")  # Set window dimensions
main_window.resizable(False, False)  # Disable window resizing

# Add a border around the main window
main_window.configure(borderwidth=5, relief='ridge')

entry_name = Entry(main_window)
entry_name.grid(column=1, row=0, padx=10, pady=5)
entry_item = Entry(main_window)
entry_item.grid(column=1, row=1, padx=10, pady=5)
entry_hires = Entry(main_window)
entry_hires.grid(column=1, row=2, padx=10, pady=5)
delete_item = Entry(main_window)
delete_item.grid(column=3, row=3, padx=10, pady=5)

main()
