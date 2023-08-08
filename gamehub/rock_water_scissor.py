from tkinter import *
import random

choices = ["rock", "paper", "scissors"]

def which_button(button_press):
    main_function(button_press)

def disable_window():
    window.destroy()

"""def reset_game():
    button1["state"] = "active"
    button2["state"] = "active"
    button3["state"] = "active"
    #l1.config(text = "Player ")
    #l3.config(text = "Computer")
    #l4.config(text = "")
     """

def main_function(player):

    output_win = Tk()
    output_win.title("Output Window")
    output_win.resizable(False, False)
    computer = random.choice(choices)

    if player == computer:
        label1 = Label(output_win,
                       text= "Player : " + str(player) + "\n\nComputer : " + str(computer) + "\n\n TIE",
                       font=("Times New Roman", 15),
                       fg="#293556",
                       bg="#cbd1e7",
                       activeforeground="#293556",
                       activebackground="#cbd1e7",
                       ).pack()
        output_win.after(5000, lambda : output_win.destroy())

    elif player == "rock":
        if computer == "paper":
            label2 = Label(output_win,
                           text="Player : " + str(player) + "\n\nComputer : " + str(computer) + "\n\n YOU LOSE!",
                           font=("Times New Roman", 15),
                           fg="#293556",
                           bg="#cbd1e7",
                           activeforeground="#293556",
                           activebackground="#cbd1e7",
                           ).pack()
            output_win.after(5000, lambda: output_win.destroy())

        elif computer == "scissors":
            label3 = Label(output_win,
                           text="Player : " + str(player) + "\n\nComputer : " + str(computer) + "\n\n YOU WIN!",
                           font=("Times New Roman", 15),
                           fg="#293556",
                           bg="#cbd1e7",
                           activeforeground="#293556",
                           activebackground="#cbd1e7",
                           ).pack()
            output_win.after(5000, lambda: output_win.destroy())

    elif player == "paper":
        if computer == "rock":
            label4 = Label(output_win,
                           text="Player : " + str(player) + "\n\nComputer : " + str(computer) + "\n\n YOU WIN!",
                           font=("Times New Roman", 15),
                           fg="#293556",
                           bg="#cbd1e7",
                           activeforeground="#293556",
                           activebackground="#cbd1e7",
                           ).pack()
            output_win.after(5000, lambda: output_win.destroy())

        elif computer == "scissors":
            label5 = Label(output_win,
                           text="Player : " + str(player) + "\n\nComputer : " + str(computer) + "\n\n YOU LOSE!",
                           font=("Times New Roman", 15),
                           fg="#293556",
                           bg="#cbd1e7",
                           activeforeground="#293556",
                           activebackground="#cbd1e7",
                           ).pack()
            output_win.after(5000, lambda: output_win.destroy())

    elif player == "scissors":
        if computer == "rock":
            label6 = Label(output_win,
                           text="Player : " + str(player) + "\n\nComputer : " + str(computer) + "\n\n YOU LOSE!",
                           font=("Times New Roman", 15),
                           fg="#293556",
                           bg="#cbd1e7",
                           activeforeground="#293556",
                           activebackground="#cbd1e7",
                           ).pack()
            output_win.after(5000, lambda: output_win.destroy())

        elif computer == "paper":
            label7 = Label(output_win,
                           text="Player : " + str(player) + "\n\nComputer : " + str(computer) + "\n\n YOU WIN!",
                           font=("Times New Roman", 15),
                           fg="#293556",
                           bg="#cbd1e7",
                           activeforeground="#293556",
                           activebackground= "#cbd1e7",
                           ).pack()
            output_win.after(5000, lambda: output_win.destroy())

window = Tk()

window.geometry("1200x700")
window.title("Rock Paper Scissor")
window.resizable(True, True)
window.config(bg="#647bb4")

rock = PhotoImage(file = "rock.png")
paper = PhotoImage(file = "paper.png")
scissor = PhotoImage(file = "scissor.png")

button1 = Button(window,
                 text = "Rock",
                 font=("Times New Roman",20),
                 fg = "white",
                 bg = "#293556",
                 activeforeground="white",
                 activebackground="#293556",
                 image= rock,
                 compound="left",
                 command=lambda text = "rock" : which_button(text))
button1.pack(pady=20)

button2 = Button(window,
                 text = "Paper",
                 font=("Times New Roman",20),
                 fg = "white",
                 bg = "#293556",
                 activeforeground="white",
                 activebackground="#293556",
                 image=paper,
                 compound="left",
                 command=lambda text = "paper" : which_button(text)
                 )
button2.pack(pady=20)

button3 = Button(window,
                 text = "Scissor",
                 font=("Times New Roman",20),
                 fg = "white",
                 bg = "#293556",
                 activeforeground="white",
                 activebackground="#293556",
                 image=scissor,
                 compound="left",
                 command=lambda text = "scissors" : which_button(text)
                 ).pack(pady=20)

quit_button = Button(window,
                     text = "Quit",
                     command= disable_window,
                     font=("Times New Roman", 20),
                     fg="#324067",
                     bg="#cccc00",
                     activeforeground="#324067",
                     activebackground="#cccc00"
                     ).pack(pady=20)

window.mainloop()