import manufacturer
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

# Creating the SPRINT1 database and Manufacturer table
manufacturer.create_sprint1_db()
manufacturer.connect_sprint1_db()
manufacturer.create_manufacturer_table()

# Method when button 'Add Manufacturer' clicked
def clickedAdd():
    label = Label() # placeholder

# Method when button 'Delete Manufacturer' clicked
def clickedEdit():
    label = Label() # placeholder

# Method when button 'Display Manufacturer' clicked
def clickedDisplay():
    label = Label() # placeholder

# Method when button 'Submit' clicked
def clickedSubmit():
    ManufacturerID = int(entryManufacturerID.get())
    ManufacturerFirstName = entryManufacturerFirstName.get()
    ManufacturerLastName = entryManufacturerLastName.get()
    ManufacturerItem = entryManufacturerItem.get()
    ManufacturerStreetAddress = entryManufacturerStreetAddress.get()
    ManufacturerPhoneNumber = int(entryManufacturerPhoneNumber.get())

    manufacturer.add_manufacturer(ManufacturerID, ManufacturerFirstName, ManufacturerLastName, ManufacturerItem, ManufacturerStreetAddress, ManufacturerPhoneNumber)

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
moduleName = Label(leftFrame, text="Manufacturer\nManagement", bg=blue, fg=white, font=('Calibri', 26, BOLD))
moduleName.place(x=120, y=80, anchor="center")

# Show as line
lineLabel = Label(leftFrame, bg=orange)
lineLabel.place(x=120, y=160, anchor="center", width=195, height=3)

# Button
btnAdd = Button(leftFrame, text="Add\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedAdd, activebackground='#FB5F00', activeforeground=white)
btnAdd.place(x=120, y=260, anchor="center", width=160, height=100)
btnEdit = Button(leftFrame, text="Delete\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedEdit, activebackground='#FB5F00', activeforeground=white)
btnEdit.place(x=120, y=400, anchor="center", width=160, height=100)
btnDisplay = Button(leftFrame, text="Display\nManufacturer", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedDisplay, activebackground='#FB5F00', activeforeground=white)
btnDisplay.place(x=120, y=540, anchor="center", width=160, height=100)

# Title of the page
titlePadX = (( screen_width-240-252 )/2)
labelTitle = Label(window, text="Add Manufacturer", font=('Arial', 30, BOLD), fg=blue)
labelTitle.grid(column=1, row=0, columnspan=5, padx=titlePadX)

# Back button
btnBack = Button(window, text="Back", font=('Arial', 14), bg=orange, fg=white, relief='flat', command=clickedBack, activebackground='#FB5F00', activeforeground=white)
btnBack.grid(column=1, row=0, ipadx=10, ipady=2)

# Main function
# Frame
inputFrame = Frame(window, width=1000)
inputFrame.grid(column=1, row=2, columnspan=5, rowspan=7, sticky="ns")

# Label
labelManufacturerID = Label(inputFrame, text="ID :", font=('Arial', 24), fg=blue)
labelManufacturerID.place(x=300, y=30, anchor="e")
labelManufacturerFirstName = Label(inputFrame, text="First Name :", font=('Arial', 24), fg=blue)
labelManufacturerFirstName.place(x=300, y=110, anchor="e")
labelManufacturerLastName = Label(inputFrame, text="Last Name :", font=('Arial', 24), fg=blue)
labelManufacturerLastName.place(x=300, y=190, anchor="e")
labelManufacturerItem = Label(inputFrame, text="Item :", font=('Arial', 24), fg=blue)
labelManufacturerItem.place(x=300, y=270, anchor="e")
labelManufacturerStreetAddress = Label(inputFrame, text="Street Address :", font=('Arial', 24), fg=blue)
labelManufacturerStreetAddress.place(x=300, y=350, anchor="e")
labelManufacturerPhoneNumber = Label(inputFrame, text="Phone Number :", font=('Arial', 24), fg=blue)
labelManufacturerPhoneNumber.place(x=300, y=500, anchor="e")

# Entry
entryManufacturerID = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryManufacturerID.place(x=310, y=30, anchor="w", width=470, height=50)
entryManufacturerFirstName = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryManufacturerFirstName.place(x=310, y=110, anchor="w", width=470, height=50)
entryManufacturerLastName = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryManufacturerLastName.place(x=310, y=190, anchor="w", width=470, height=50)
entryManufacturerItem = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryManufacturerItem.place(x=310, y=270, anchor="w", width=470, height=50)
entryManufacturerStreetAddress = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryManufacturerStreetAddress.place(x=310, y=390, anchor="w", width=470, height=125)
entryManufacturerPhoneNumber = Entry(inputFrame, font=('Arial', 24), fg=white, bg=blue)
entryManufacturerPhoneNumber.place(x=310, y=500, anchor="w", width=470, height=50)

# Submit button
btnSubmit = Button(window, text="Submit", font=('Arial', 18), bg=orange, fg=white, relief='flat', command=clickedSubmit, activebackground='#FB5F00', activeforeground=white)
btnSubmit.grid(column=1, row=8, columnspan=5, ipadx=35, ipady=5)
  
window.mainloop()