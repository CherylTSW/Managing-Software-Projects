from lib import authentication as auth
from lib import database as db
from lib import inventory
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

db_host = "localhost"
db_user = "root"
db_pwd = ""
auth_db = "Authentication"

auth_db_conn = db.create_db_connection(db_host , db_user, db_pwd, auth_db)

# Add an account 
auth.add_account(auth_db_conn, "placeholder", "123", "pol", "tato", 1)

# Delete an account with userID
auth.delete_account(auth_db_conn, auth.get_userID(auth_db_conn, "placeholder"))

'''
    -KhaHau-
    Below are codes for creating GUI(Add Inventory)
    Will need compiling when other GUI codes are added in
    Comment: Codes for generating UI moved into method(activated by button click to load the UI)
'''
# Method when button 'Add Inventory' clicked
def clickedAdd():
    label = Label() # placeholder

# Method when button 'Edit Inventory' clicked
def clickedEdit():
    label = Label() # placeholder

# Method when button 'Display Inventory' clicked
def clickedDisplay():
    label = Label() # placeholder

# Method when button 'Submit' clicked
def clickedSubmit():
    itemName = entryItemName.get()
    price = float(entryPrice.get())
    quantity = int(entryQuantity.get())

    if(inventory.add_inventory(itemName, price, quantity)):
        entryItemName.delete(0, 'end')
        entryPrice.delete(0, 'end')
        entryQuantity.delete(0, 'end')
        messagebox.showinfo('', 'Item added into inventory successfully !')

# Method when button 'Back' clicked
def clickedBack():
    label = Label() # placeholder (Not to implement in this Sprint)

# Create window
window = Tk()
window.attributes('-fullscreen', True)
screen_width = window.winfo_screenwidth()        
screen_height = window.winfo_screenheight()

# Color code
blue = "#344955"
white = "#ffffff"
orange = "#fb8000"

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

# Title of the page
titlePadX = (( screen_width-240-252 )/2)
labelTitle = Label(window, text="Add Inventory", font=('Arial', 30, BOLD), fg=blue)
labelTitle.grid(column=1, row=0, columnspan=5, padx=titlePadX)

# Back button
btnBack = Button(window, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white)
btnBack.grid(column=1, row=0, ipadx=10, ipady=2)

# Main function 
# Frame
inputFrame = Frame(window, width=1000)
inputFrame.grid(column=1, row=2, columnspan=5, rowspan=4, sticky="ns")
# Label
labelItemName = Label(inputFrame, text="Item Name :", font=('Arial', 24), fg=blue)
labelItemName.place(x=300, y=60, anchor="e")
labelPrice = Label(inputFrame, text="Price :", font=('Arial', 24), fg=blue)
labelPrice.place(x=300, y=160, anchor="e")
labelQuantity = Label(inputFrame, text="Quantity :", font=('Arial', 24), fg=blue)
labelQuantity.place(x=300, y=260, anchor="e")
# Entry
entryItemName = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryItemName.place(x=310, y=60, anchor="w", width=470, height=50)
entryPrice = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryPrice.place(x=310, y=160, anchor="w", width=470, height=50)
entryQuantity = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryQuantity.place(x=310, y=260, anchor="w", width=470, height=50)

# Submit button
btnSubmit = Button(window, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white)
btnSubmit.grid(column=1, row=8, columnspan=5, ipadx=35, ipady=5)
  
window.mainloop()