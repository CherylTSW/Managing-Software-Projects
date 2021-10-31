
from lib import inventory
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD


'''
    Inventory Module
'''

# Method when button 'Add Inventory' clicked
def clickedAdd():
    # The left navigation panel
    # Frame
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
    leftFrame.grid(column=0, row=0, rowspan=10)
    leftFrame.grid_propagate(0)
    # Label
    moduleName = Label(leftFrame, text="Inventory\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
    moduleName.place(x=120, y=80, anchor="center")
    # Show as line
    lineLabel = Label(leftFrame, bg=orange)
    lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
    # Button
    btnAdd = Button(leftFrame, text="Add\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
    btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
    btnEdit = Button(leftFrame, text="Edit\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedEdit, activebackground='#FB5F00', activeforeground=white)
    btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
    btnDisplay = Button(leftFrame, text="Display\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
    btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

    # Main function
    
    # Method when button 'Submit' clicked
    def clickedSubmit():
        if(len(entryItemName.get()) != 0 and len(entryPrice.get()) != 0 and len(entryQuantity.get()) != 0):
            itemName = entryItemName.get()
            price = float(entryPrice.get())
            quantity = int(entryQuantity.get())

            if(inventory.add_inventory(itemName, price, quantity)):
                entryItemName.delete(0, 'end')
                entryPrice.delete(0, 'end')
                entryQuantity.delete(0, 'end')
                messagebox.showinfo('', 'Item added into inventory successfully !')
            else:
                messagebox.showerror('Error', 'An error occured while trying to add the item into inventory')
        else:
            messagebox.showerror('Error', 'Please fill in all the fields')
    
    # Frame
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
    inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
    # Title of the page
    labelTitle = Label(inputFrame, text="Add Inventory", font=('Arial', 30, BOLD), fg=blue)
    labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
    # Back button
    btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
    btnBack.place(x=50, y=70, anchor='w')
    # Label
    labelItemName = Label(inputFrame, text="Item Name :", font=('Arial', 24), fg=blue)
    labelItemName.place(x=x_offset, y=270, anchor="e")
    labelPrice = Label(inputFrame, text="Price(RM) :", font=('Arial', 24), fg=blue)
    labelPrice.place(x=x_offset, y=370, anchor="e")
    labelQuantity = Label(inputFrame, text="Quantity :", font=('Arial', 24), fg=blue)
    labelQuantity.place(x=x_offset, y=470, anchor="e")
    # Entry
    entryItemName = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    entryItemName.place(x=x_offset+10, y=270, anchor="w", width=470, height=50)
    entryPrice = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    entryPrice.place(x=x_offset+10, y=370, anchor="w", width=470, height=50)
    entryQuantity = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    entryQuantity.place(x=x_offset+10, y=470, anchor="w", width=470, height=50)
    # Submit button
    btnSubmit = Button(inputFrame, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
    btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

# Method when button 'Edit Inventory' clicked
def clickedEdit():
    # The left navigation panel
    # Frame
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
    leftFrame.grid(column=0, row=0, rowspan=10)
    leftFrame.grid_propagate(0)
    # Label
    moduleName = Label(leftFrame, text="Inventory\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
    moduleName.place(x=120, y=80, anchor="center")
    # Show as line
    lineLabel = Label(leftFrame, bg=orange)
    lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
    # Button
    btnAdd = Button(leftFrame, text="Add\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
    btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
    btnEdit = Button(leftFrame, text="Edit\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedEdit, activebackground='#FB5F00', activeforeground=white)
    btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
    btnDisplay = Button(leftFrame, text="Display\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
    btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

    # Main function

    # Method when button 'Submit' clicked
    def clickedSubmit():
        if( len(entryItemID.get()) != 0 and len(entryItemName.get()) != 0 and len(entryPrice.get()) != 0 and len(entryQuantity.get()) != 0):
            itemID = int(entryItemID.get())
            itemName = entryItemName.get()
            price = float(entryPrice.get())
            quantity = int(entryQuantity.get())
            
            if(inventory.edit_inventory(itemName, price, quantity, itemID)):
                entryItemID.delete(0, 'end')
                entryItemName.delete(0, 'end')
                entryPrice.delete(0, 'end')
                entryQuantity.delete(0, 'end')
                messagebox.showinfo('', 'Item Edited successfully !')
            else:
                messagebox.showerror('Error', 'An error occured while trying to edit the item')
        else:
            messagebox.showerror('Error', 'Please fill in all the fields')

    # Frame
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
    inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
    # Title of the page
    labelTitle = Label(inputFrame, text="Edit Inventory", font=('Arial', 30, BOLD), fg=blue)
    labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
    # Back button
    btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
    btnBack.place(x=50, y=70, anchor='w')
    # Label
    labelItemID = Label(inputFrame, text="Item ID :", font=('Arial', 24), fg=blue)
    labelItemID.place(x=x_offset, y=270, anchor="e")
    labelItemName = Label(inputFrame, text="New Item Name :", font=('Arial', 24), fg=blue)
    labelItemName.place(x=x_offset, y=370, anchor="e")
    labelPrice = Label(inputFrame, text="New Price(RM) :", font=('Arial', 24), fg=blue)
    labelPrice.place(x=x_offset, y=470, anchor="e")
    labelQuantity = Label(inputFrame, text="New Quantity :", font=('Arial', 24), fg=blue)
    labelQuantity.place(x=x_offset, y=570, anchor="e")
    # Entry
    entryItemID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    entryItemID.place(x=x_offset+10, y=270, anchor="w", width=470, height=50)
    entryItemName = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    entryItemName.place(x=x_offset+10, y=370, anchor="w", width=470, height=50)
    entryPrice = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    entryPrice.place(x=x_offset+10, y=470, anchor="w", width=470, height=50)
    entryQuantity = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    entryQuantity.place(x=x_offset+10, y=570, anchor="w", width=470, height=50)
    # Submit button
    btnSubmit = Button(inputFrame, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
    btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

# Method when button 'Display Inventory' clicked
def clickedDisplay():
    # The left navigation panel
    # Frame
    leftFrame = Frame(window, bg=blue, width=240, height=screen_height)
    leftFrame.grid(column=0, row=0, rowspan=10)
    leftFrame.grid_propagate(0)
    # Label
    moduleName = Label(leftFrame, text="Inventory\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
    moduleName.place(x=120, y=80, anchor="center")
    # Show as line
    lineLabel = Label(leftFrame, bg=orange)
    lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
    # Button
    btnAdd = Button(leftFrame, text="Add\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
    btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
    btnEdit = Button(leftFrame, text="Edit\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedEdit, activebackground='#FB5F00', activeforeground=white)
    btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
    btnDisplay = Button(leftFrame, text="Display\nInventory", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
    btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

    # Main function
    
    # Method when button 'Submit' clicked
    def clickedSubmit():
        if( len(entryItemID.get()) != 0 ): 
            itemID = int(entryItemID.get())
            result = inventory.get_inventory_by_id(itemID)
            if(result):
                inventory.display_inventory(inputFrame, 150, 500, result)
            else:
                messagebox.showerror('Match not found', 'No match can be found')
            
        elif(len(entryItemName.get()) != 0):
            itemName = entryItemName.get()
            result = inventory.get_inventory_by_name(itemName)
            if(result):
                inventory.display_inventory(inputFrame, 150, 500, result)
            else:
                messagebox.showerror('Match not found', 'No match can be found')
        else:
            messagebox.showerror('Error', 'Please fill in the Item ID or Item Name to be searched')

    # Frame
    inputFrame = Frame(window, width=screen_width-240, height=screen_height)
    inputFrame.grid(column=1, row=0, rowspan=10, sticky="ns")
    # Title of the page
    labelTitle = Label(inputFrame, text="Display Inventory", font=('Arial', 30, BOLD), fg=blue)
    labelTitle.place(x=(screen_width-240)/2, y=70, anchor='center')
    # Back button
    btnBack = Button(inputFrame, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white, padx=20, pady=5)
    btnBack.place(x=50, y=70, anchor='w')
    # Label
    labelItemID = Label(inputFrame, text="Item ID :", font=('Arial', 24), fg=blue)
    labelItemID.place(x=x_offset, y=270, anchor="e")
    labelItemName = Label(inputFrame, text="Item Name :", font=('Arial', 24), fg=blue)
    labelItemName.place(x=x_offset, y=370, anchor="e")
    # Entry
    entryItemID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    entryItemID.place(x=x_offset+10, y=270, anchor="w", width=470, height=50)
    entryItemName = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
    entryItemName.place(x=x_offset+10, y=370, anchor="w", width=470, height=50)
    # Submit button
    btnSubmit = Button(inputFrame, text="Search", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white, padx=30, pady=5)
    btnSubmit.place(x=(screen_width-240)/2, y=800, anchor='center')

# Method when button 'Back' clicked
def clickedBack():
    frame = Frame(window, width=screen_width, height=screen_height, bg=white)
    frame.grid(column=0, row=0, columnspan=2, rowspan=10)
    btnTest = Button(frame, text="GO", font=('Arial', 18), command=clickedAdd)
    btnTest.grid(column=0, row=0, in_=frame)
    frame.grid_propagate(0)
    frame.lift()

# Color code
blue = "#344955"
white = "#ffffff"
orange = "#fb8000"

# Main program
# Create window
window = Tk()
window.attributes('-fullscreen', True)
screen_width = window.winfo_screenwidth()        
screen_height = window.winfo_screenheight()
# X offset calculation
x_offset = int((screen_width-240-780)/2 + 250)
# Create database and table
inventory.create_inventory_db()
inventory.execute_sql_file("sql/InventoryDB.sql")
# Testing purpose button
btnTest = Button(window, text="GO", font=('Arial', 18), command=clickedAdd)
btnTest.grid(column=0, row=0)
  
window.mainloop()