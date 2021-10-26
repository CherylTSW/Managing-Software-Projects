import contact
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

contact.create_database()
contact.connect_contact_db()
contact.create_contact_table()

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
    orderId = int(entryOrderID.get())
    price = float(entryPrice.get())
    quantity = int(entryQuantity.get())
    orderDate = entryOrderDate.get()
    manufacturerId = int(entryManufacturerID.get())
    productId = int(entryProductID.get())

    contact.insert_contact(orderId, orderDate, manufacturerId, productId, quantity, price)

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
moduleName = Label(leftFrame, text="Contact Module\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
moduleName.place(x=120, y=80, anchor="center")
# Show as line
lineLabel = Label(leftFrame, bg=orange)
lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)
# Button
btnAdd = Button(leftFrame, text="Add\nContact Module", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
btnEdit = Button(leftFrame, text="Edit\nContact Module", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedEdit, activebackground='#FB5F00', activeforeground=white)
btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
btnDisplay = Button(leftFrame, text="Display\nContact Module", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

# Title of the page
titlePadX = (( screen_width-240-252 )/2)
labelTitle = Label(window, text="Add Contact Module", font=('Arial', 30, BOLD), fg=blue)
labelTitle.grid(column=1, row=0, columnspan=5, padx=titlePadX)

# Back button
btnBack = Button(window, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white)
btnBack.grid(column=1, row=0, ipadx=10, ipady=2)

# Main function 
# Frame
inputFrame = Frame(window, width=1000)
inputFrame.grid(column=1, row=2, columnspan=5, rowspan=7, sticky="ns")
# Label
labelOrderId = Label(inputFrame, text="Order ID :", font=('Arial', 24), fg=blue)
labelOrderId.place(x=300, y=30, anchor="e")
labelOrderDate = Label(inputFrame, text="Order Date :", font=('Arial', 24), fg=blue)
labelOrderDate.place(x=300, y=100, anchor="e")
labelManufacturerId = Label(inputFrame, text="Manufacturer ID :", font=('Arial', 24), fg=blue)
labelManufacturerId.place(x=300, y=170, anchor="e")
labelProductId = Label(inputFrame, text="Product ID :", font=('Arial', 24), fg=blue)
labelProductId.place(x=300, y=240, anchor="e")
labelQuantity = Label(inputFrame, text="Quantity :", font=('Arial', 24), fg=blue)
labelQuantity.place(x=300, y=310, anchor="e")
labelPrice = Label(inputFrame, text="Total Price :", font=('Arial', 24), fg=blue)
labelPrice.place(x=300, y=380, anchor="e")

# Entry
entryOrderID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryOrderID.place(x=310, y=30, anchor="w", width=470, height=50)
entryOrderDate = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryOrderDate.place(x=310, y=100, anchor="w", width=470, height=50)
entryManufacturerID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryManufacturerID.place(x=310, y=170, anchor="w", width=470, height=50)
entryProductID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryProductID.place(x=310, y=240, anchor="w", width=470, height=50)
entryQuantity = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryQuantity.place(x=310, y=310, anchor="w", width=470, height=50)
entryPrice = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryPrice.place(x=310, y=380, anchor="w", width=470, height=50)

# Submit button
btnSubmit = Button(window, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white)
btnSubmit.grid(column=1, row=8, columnspan=5, ipadx=35, ipady=5)
  
window.mainloop()