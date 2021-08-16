__author__ = "Vujic Dejan"

from tkinter import *
import random
import string

root = Tk()
root.title("Password generator")
root.iconbitmap('assets/icon.png')
root.geometry("550x550")
root.config(bg = "#383e56") 
root.resizable(width=FALSE, height=FALSE)


# Functions
def choice_selection(): #sel
    selection = choice.get()
choice = IntVar()


def callback():
    password_entry.config(text = password_generate())


def password_generate():
    if choice.get() == 1:
        return "".join(random.sample(basic, characters.get()))
    elif choice.get() == 2:
        return "".join(random.sample(medium, characters.get()))
    elif choice.get() == 3:
        return "".join(random.sample(extra, characters.get()))


basic = string.ascii_uppercase + string.ascii_lowercase 
medium = string.ascii_uppercase + string.ascii_lowercase + string.digits 
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/""" 
extra = basic + medium + symbols 


# Interface
# Frame Title
label_title = Label( text = "Password Generator", bg="#383e56", 
                     fg = "#F1DE8F", font = ("Helvetica", 35, "bold") )
label_title.pack(pady=20)


# Frame characters text before input
label_before_input = Label( text = "Enter the length of your password", bg = "#383e56",
                            fg = "#F1DE8F", font = ("Helvetica", 15, "bold") )
label_before_input.pack(pady=20)


# Spinbox for length of characters
characters = IntVar()
characters_box = Spinbox( from_=8, to_=50, textvariable=characters, bg="#B3BAD2", 
                          font=("Helvetica, 15"), fg="#FFF75E")
characters_box.config( highlightbackground = "#B3BAD2",
                   highlightcolor = "#B3BAD2")
characters_box.pack(pady=20)


# Label text strength
label_strength = Label( text = "Choose the strength of your password", bg = "#383e56",
                            fg = "#F1DE8F", font = ("Helvetica", 15, "bold") )
label_strength.pack(pady=20)


# Choice part
choice_frame = Frame(root, bg = "#383e56")
choice_frame.pack(pady=20)

R1 = Radiobutton( choice_frame, font=("Helvetica", 15, "bold"), text="BASIC", bg="#383e56", 
                  fg="#F1DE8F", variable=choice, value=1, command=choice_selection).grid(row=0, 
                  column= 0, padx=10)
R2 = Radiobutton( choice_frame, font=("Helvetica", 15, "bold"), text="MEDIUM", bg="#383e56", 
                  fg="#F1DE8F", variable=choice, value=2, command=choice_selection).grid(row=0, 
                  column = 1, padx=10)
R3 = Radiobutton( choice_frame, font=("Helvetica", 15, "bold"), text="EXTRA", bg="#383e56", 
                  fg="#F1DE8F", variable=choice, value=3, command=choice_selection).grid(row=0, 
                  column = 2, padx=10)

labelchoice = Label(choice_frame, bg="#383e56", fg="#F1DE8F") 


# Label for returned password
password_entry = Label( root, text="", font = ('Helvetica', 24, "bold"), 
                        bd=0, bg="#383e56", fg="#FFF75E")
password_entry.config( highlightbackground = "#383e56",
                       highlightcolor = "#383e56", justify='center')
password_entry.pack(pady=20, side=BOTTOM)


# Buttons Frame
buttons_frame = Frame(root, bg = "#383e56")
buttons_frame.pack(pady=20)

# Buttons
generate_button = Button( buttons_frame, text = "Generate your password", command=callback,
                          bg="#B3BAD2", height=3, width=25, font=("Helvetica", 15))
generate_button.grid(row = 0, column = 0, padx = 10)


root.mainloop()
