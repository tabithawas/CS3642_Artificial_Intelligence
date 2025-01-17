# Course:       CS 3642
# Assignment #: 1
# Due Date:     9/16/24

from tkinter import *

# Initial value for balance and output 
balance = 0
output = ""

# Setup tkinter root 
root = Tk()
root.title("Assignment #1 - Coca Cola Vending Machine")
root.configure(height=650, width=750)

# Set images needed for GUI 
img_background = PhotoImage(file="./gui_imgs/gui_background.png") 
img_quarter = PhotoImage(file="./gui_imgs/resized_quarter.png") 
img_dime = PhotoImage(file="./gui_imgs/resized_dime.png") 
img_nickel = PhotoImage(file="./gui_imgs/resized_nickel.png") 

# Update the output and balance labels 
def update_labels(): 
    # Get text for output label 
    get_output_text()

    # Use global variables 
    global balance 
    global output

    # Update the balance and output labels  
    label_balance.config(text=balance)
    label_output.config(text=output)

    # Print output as needed 
    if (output != ""): 
        print("Output:", output, "\n")

# Get the text for the output label  
def get_output_text(): 
    # Use global variables 
    global balance
    global output

    # Check the current change value 
    change = balance - 30 

    # Set balance and output if change is or is not due 
    if (change >= 0): 
        balance = 0
    else: 
        output = ""

    # Set output text based on amount of change due 
    if (change == 0): 
        output = "Coke, no change"
    elif (change == 5): 
        output = "Coke, nickel"
    elif (change == 10): 
        output = "Coke, dime"
    elif (change == 15): 
        output = "Coke, nickel, dime"
    elif (change == 20): 
        output = "Coke, dime, nickel, nickel"

# Add 25 cents to the balance if the quarter button is clicked 
def clicked_quarter():
    global balance
    balance += 25
    print("Input: Quarter")
    update_labels()

# Add 10 cents to the balance if the dime button is clicked 
def clicked_dime(): 
    global balance
    balance += 10
    print("Input: Dime")
    update_labels()

# Add 5 cents to the balance if the nickel button is clicked 
def clicked_nickel(): 
    global balance
    balance += 5
    print("Input: Nickel")
    update_labels()

# Place the background GUI image 
background = Label(root, image=img_background)
background.place(x=0, y=0)

# Place the coin buttons 
button_quarter = Button(root, image=img_quarter, command=clicked_quarter)
button_quarter.place(x=490, y=100)

button_dime = Button(root, image=img_dime, command=clicked_dime)
button_dime.place(x=490, y=200)

button_nickel = Button(root, image=img_nickel, command=clicked_nickel)
button_nickel.place(x=490, y=300)

# Place the balance and output labels 
label_balance = Label(root, text=balance, font="Sans", background="gray", width=10)
label_balance.place(x=215, y=232)

label_cents = Label(root, text="cents", font="Sans", background="gray", width=10)
label_cents.place(x=215, y=252)

label_output = Label(root, text=output, font="Sans", background="gray", width=59, height=2)
label_output.place(x=100, y=525)

# Call the mainloop 
root.mainloop()