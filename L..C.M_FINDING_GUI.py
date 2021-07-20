from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("L.C.M finding gui")
# the below is the main defination that finds lcm
def findlcm (a, b):
    while(True):
        if (a) :
            a = maxi
        if int(maxi % a == 0 and maxi % b == 0):
            lcm = a;
            break;
        maxi = maxi + 1
    return lcm

# Help lol!!
def help_given_to_the_user():
    messagebox.showinfo("help","for further details pls contract sdsriram@gmal.com")

# Prints the lcm
def ans_lcm():
    lcm = findlcm(l_num1, l_num2)
    ans_label = Label(int(root,text= lcm))
    ans_label.grid(row=5,column=1,font=("word",24))


# the GUI Part
heading = Label(root,text="L.CM FINDER",font=("word", 24))
heading.grid(row=0,column=0)

heading1 = Label(root,text="1 numder : ",font=("word", 24))
heading1.grid(row=1,column=0)

heading2 = Label(root,text="2 number: ",font=("word", 24))
heading2.grid(row=2,column=0)

l_num1 = IntVar()
entry = Entry(root)
entry.grid(row= 1,column=1)
l_num1 = entry.get()

l_num2 = IntVar()
entry1 = Entry(root)
entry1.grid(row=2,column=1)
l_num2 = entry1.get()


button_go = Button(root,text="find lcm",font =("word",24),command=ans_lcm)
button_go.grid(row=3,column=1,pady=20,padx=40)

button_go = Button(root,text="help",font =("word",24),command=help_given_to_the_user)
button_go.grid(row=3,column=0,pady=20,padx=40)
# GUI Ends----------------------------------------------------------------------------------------

root.mainloop()
# END------

# dad i made this project there is a error in the while finding the lcm
# pls fix this syntax error DAD
# it says intvar........
#
