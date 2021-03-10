from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title("ticktacktoe2")
#window.geometry("300x300")
def select_choice_X(btn):
    btn["text"] = "X"

def select_choice_O(btn):
    btn["text"] = "O"
"""
when button is clicked the first time then the turn is 0 ad so the function
turns is called and since 0 is the same as index 0, the button displays X
in the button text. And then the function stops running and somehow remembers
this. Then the next time another button is clicked the function runs again with
the turn being 1.
"""
# first button clicked: display X
# second button clicked: display O
turn = True
def turns(btn):
    global turn
    if btn["text"] == "" and turn == True:
        select_choice_X(btn)
        turn = False
        check_winner(btn)
    elif btn["text"] == "" and turn == False:
        select_choice_O(btn)
        turn = True
        check_winner(btn)
    #else:
    #    messagebox.showerror("ticktacktoe", "Click another box")

def disable_btns():
    btn_1.state(['disabled'])
    btn_2.state(['disabled'])
    btn_3.state(['disabled'])
    btn_4.state(['disabled'])
    btn_5.state(['disabled'])
    btn_6.state(['disabled'])
    btn_7.state(['disabled'])
    btn_8.state(['disabled'])
    btn_9.state(['disabled'])

def check_winner(btn):
    #possible win combination for X
    win_comp_X_1 = btn_1["text"] == "X" and btn_2["text"] == "X" and btn_3["text"] == "X"
    win_comp_X_2 = btn_4["text"] == "X" and btn_5["text"] == "X" and btn_6["text"] == "X"
    win_comp_X_3 = btn_7["text"] == "X" and btn_8["text"] == "X" and btn_9["text"] == "X"
    win_comp_X_4 = btn_1["text"] == "X" and btn_4["text"] == "X" and btn_7["text"] == "X"
    win_comp_X_5 = btn_2["text"] == "X" and btn_5["text"] == "X" and btn_8["text"] == "X"
    win_comp_X_6 = btn_3["text"] == "X" and btn_6["text"] == "X" and btn_9["text"] == "X"
    win_comp_X_7 = btn_1["text"] == "X" and btn_5["text"] == "X" and btn_9["text"] == "X"
    win_comp_X_8 = btn_3["text"] == "X" and btn_5["text"] == "X" and btn_7["text"] == "X"
    #possible win combinations for O
    win_comp_O_1 = btn_1["text"] == "O" and btn_2["text"] == "O" and btn_3["text"] == "O"
    win_comp_O_2 = btn_4["text"] == "O" and btn_5["text"] == "O" and btn_6["text"] == "O"
    win_comp_O_3 = btn_7["text"] == "O" and btn_8["text"] == "O" and btn_9["text"] == "O"
    win_comp_O_4 = btn_1["text"] == "O" and btn_4["text"] == "O" and btn_7["text"] == "O"
    win_comp_O_5 = btn_2["text"] == "O" and btn_5["text"] == "O" and btn_8["text"] == "O"
    win_comp_O_6 = btn_3["text"] == "O" and btn_6["text"] == "O" and btn_9["text"] == "O"
    win_comp_O_7 = btn_1["text"] == "O" and btn_5["text"] == "O" and btn_9["text"] == "O"
    win_comp_O_8 = btn_3["text"] == "O" and btn_5["text"] == "O" and btn_7["text"] == "O"

    if win_comp_X_1:
        messagebox.showinfo("tick tack toe", "Player X Wins!")
        disable_btns()
    elif win_comp_X_2:
        messagebox.showinfo("tick tack toe", "Player X Wins!")
        disable_btns()
    elif win_comp_X_3:
        messagebox.showinfo("tick tack toe", "Player X Wins!")
        disable_btns()
    elif win_comp_X_4:
        messagebox.showinfo("tick tack toe", "Player X Wins!")
        disable_btns()
    elif win_comp_X_5:
        messagebox.showinfo("tick tack toe", "Player X Wins!")
        disable_btns()
    elif win_comp_X_6:
        messagebox.showinfo("tick tack toe", "Player X Wins!")
        disable_btns()
    elif win_comp_X_7:
        messagebox.showinfo("tick tack toe", "Player X Wins!")
        disable_btns()
    elif win_comp_X_8:
        messagebox.showinfo("tick tack toe", "Player X Wins!")
        disable_btns()

    if win_comp_O_1:
        messagebox.showinfo("tick tack toe", "Player O Wins!")
        disable_btns()
    elif win_comp_O_2:
        messagebox.showinfo("tick tack toe", "Player O Wins!")
        disable_btns()
    elif win_comp_O_3:
        messagebox.showinfo("tick tack toe", "Player O Wins!")
        disable_btns()
    elif win_comp_O_4:
        messagebox.showinfo("tick tack toe", "Player O Wins!")
        disable_btns()
    elif win_comp_O_5:
        messagebox.showinfo("tick tack toe", "Player O Wins!")
        disable_btns()
    elif win_comp_O_6:
        messagebox.showinfo("tick tack toe", "Player O Wins!")
        disable_btns()
    elif win_comp_O_7:
        messagebox.showinfo("tick tack toe", "Player O Wins!")
        disable_btns()
    elif win_comp_O_8:
        messagebox.showinfo("tick tack toe", "Player O Wins!")
        disable_btns()

#3X3 GRID
btn_1 = ttk.Button(window, text="", command=lambda: turns(btn_1))
btn_1.grid(column=0, row=0)

btn_2 = ttk.Button(window, text="", command=lambda: turns(btn_2))
btn_2.grid(column=1, row=0)

btn_3= ttk.Button(window, text="", command=lambda: turns(btn_3))
btn_3.grid(column=2, row=0)

btn_4 = ttk.Button(window, text="", command=lambda: turns(btn_4))
btn_4.grid(column=0, row=1)

btn_5 = ttk.Button(window, text="", command=lambda: turns(btn_5))
btn_5.grid(column=1, row=1)

btn_6 = ttk.Button(window, text="", command=lambda: turns(btn_6))
btn_6.grid(column=2, row=1)

btn_7 = ttk.Button(window, text="", command= lambda: turns(btn_7))
btn_7.grid(column=0, row=2)

btn_8 = ttk.Button(window, text="", command= lambda: turns(btn_8))
btn_8.grid(column=1, row=2)

btn_9 = ttk.Button(window, text="", command= lambda: turns(btn_9))
btn_9.grid(column=2, row=2)


window.mainloop()
