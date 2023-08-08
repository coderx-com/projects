from tkinter import *
from tkinter import messagebox
import random

gameopt=Tk()
gameopt.title('Choose the game you want to play')

def g_2048():
    class Board:
        bg_color = {
            '2': '#eee4da',
            '4': '#ede0c8',
            '8': '#edc850',
            '16': '#edc53f',
            '32': '#f67c5f',
            '64': '#f65e3b',
            '128': '#edcf72',
            '256': '#edcc61',
            '512': '#f2b179',
            '1024': '#f59563',
            '2048': '#edc22e',
        }
        color = {
            '2': '#776e65',
            '4': '#f9f6f2',
            '8': '#f9f6f2',
            '16': '#f9f6f2',
            '32': '#f9f6f2',
            '64': '#f9f6f2',
            '128': '#f9f6f2',
            '256': '#f9f6f2',
            '512': '#776e65',
            '1024': '#f9f6f2',
            '2048': '#f9f6f2',
        }

        def __init__(self):
            self.n = 4
            self.window = Tk()
            self.window.title('2048 Game')
            self.gameArea = Frame(self.window, bg='azure3')
            self.board = []
            self.gridCell = [[0] * 4 for i in range(4)]
            self.compress = False
            self.merge = False
            self.moved = False
            self.score = 0
            for i in range(4):
                rows = []
                for j in range(4):
                    l = Label(self.gameArea, text='', bg='azure4',
                              font=('arial', 22, 'bold'), width=4, height=2)
                    l.grid(row=i, column=j, padx=7, pady=7)
                    rows.append(l);
                self.board.append(rows)
            self.gameArea.grid()

        def reverse(self):
            for ind in range(4):
                i = 0
                j = 3
                while (i < j):
                    self.gridCell[ind][i], self.gridCell[ind][j] = self.gridCell[ind][j], self.gridCell[ind][i]
                    i += 1
                    j -= 1

        def transpose(self):
            self.gridCell = [list(t) for t in zip(*self.gridCell)]

        def compressGrid(self):
            self.compress = False
            temp = [[0] * 4 for i in range(4)]
            for i in range(4):
                cnt = 0
                for j in range(4):
                    if self.gridCell[i][j] != 0:
                        temp[i][cnt] = self.gridCell[i][j]
                        if cnt != j:
                            self.compress = True
                        cnt += 1
            self.gridCell = temp

        def mergeGrid(self):
            self.merge = False
            for i in range(4):
                for j in range(4 - 1):
                    if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                        self.gridCell[i][j] *= 2
                        self.gridCell[i][j + 1] = 0
                        self.score += self.gridCell[i][j]
                        self.merge = True

        def random_cell(self):
            cells = []
            for i in range(4):
                for j in range(4):
                    if self.gridCell[i][j] == 0:
                        cells.append((i, j))
            curr = random.choice(cells)
            i = curr[0]
            j = curr[1]
            self.gridCell[i][j] = 2

        def can_merge(self):
            for i in range(4):
                for j in range(3):
                    if self.gridCell[i][j] == self.gridCell[i][j + 1]:
                        return True

            for i in range(3):
                for j in range(4):
                    if self.gridCell[i + 1][j] == self.gridCell[i][j]:
                        return True
            return False

        def paintGrid(self):
            for i in range(4):
                for j in range(4):
                    if self.gridCell[i][j] == 0:
                        self.board[i][j].config(text='', bg='azure4')
                    else:
                        self.board[i][j].config(text=str(self.gridCell[i][j]),
                                                bg=self.bg_color.get(str(self.gridCell[i][j])),
                                                fg=self.color.get(str(self.gridCell[i][j])))

    class Game:
        def __init__(self, gamepanel):
            self.gamepanel = gamepanel
            self.end = False
            self.won = False

        def start(self):
            self.gamepanel.random_cell()
            self.gamepanel.random_cell()
            self.gamepanel.paintGrid()
            self.gamepanel.window.bind('<Key>', self.link_keys)
            self.gamepanel.window.mainloop()

        def link_keys(self, event):
            if self.end or self.won:
                return
            self.gamepanel.compress = False
            self.gamepanel.merge = False
            self.gamepanel.moved = False
            presed_key = event.keysym
            if presed_key == 'Up':
                self.gamepanel.transpose()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.transpose()
            elif presed_key == 'Down':
                self.gamepanel.transpose()
                self.gamepanel.reverse()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.reverse()
                self.gamepanel.transpose()
            elif presed_key == 'Left':
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
            elif presed_key == 'Right':
                self.gamepanel.reverse()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.reverse()
            else:
                pass
            self.gamepanel.paintGrid()
            print(self.gamepanel.score)
            flag = 0
            for i in range(4):
                for j in range(4):
                    if (self.gamepanel.gridCell[i][j] == 2048):
                        flag = 1
                        break
            if (flag == 1):  # found 2048
                self.won = True
                messagebox.showinfo('2048', message='You Wonnn!!')
                print("won")
                return
            for i in range(4):
                for j in range(4):
                    if self.gamepanel.gridCell[i][j] == 0:
                        flag = 1
                        break
            if not (flag or self.gamepanel.can_merge()):
                self.end = True
                messagebox.showinfo('2048', 'Game Over!!!')
                print("Over")
            if self.gamepanel.moved:
                self.gamepanel.random_cell()

            self.gamepanel.paintGrid()

    gamepanel = Board()
    game2048 = Game(gamepanel)
    game2048.start()

def g_rps():
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
                           text="Player : " + str(player) + "\n\nComputer : " + str(computer) + "\n\n TIE",
                           font=("Times New Roman", 15),
                           fg="#293556",
                           bg="#cbd1e7",
                           activeforeground="#293556",
                           activebackground="#cbd1e7",
                           ).pack()
            output_win.after(5000, lambda: output_win.destroy())

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
                               activebackground="#cbd1e7",
                               ).pack()
                output_win.after(5000, lambda: output_win.destroy())

    window = Tk()

    window.geometry("1200x700")
    window.title("Rock Paper Scissor")
    window.resizable(True, True)
    window.config(bg="#647bb4")

    rock = PhotoImage(file="rock.png")
    paper = PhotoImage(file="paper.png")
    scissor = PhotoImage(file="scissor.png")

    button1 = Button(window,
                     text="Rock",
                     font=("Times New Roman", 20),
                     fg="white",
                     bg="#293556",
                     activeforeground="white",
                     activebackground="#293556",
                     image=rock,
                     compound="left",
                     command=lambda text="rock": which_button(text))
    button1.pack(pady=20)

    button2 = Button(window,
                     text="Paper",
                     font=("Times New Roman", 20),
                     fg="white",
                     bg="#293556",
                     activeforeground="white",
                     activebackground="#293556",
                     image=paper,
                     compound="left",
                     command=lambda text="paper": which_button(text)
                     )
    button2.pack(pady=20)

    button3 = Button(window,
                     text="Scissor",
                     font=("Times New Roman", 20),
                     fg="white",
                     bg="#293556",
                     activeforeground="white",
                     activebackground="#293556",
                     image=scissor,
                     compound="left",
                     command=lambda text="scissors": which_button(text)
                     ).pack(pady=20)

    quit_button = Button(window,
                         text="Quit",
                         command=disable_window,
                         font=("Times New Roman", 20),
                         fg="#324067",
                         bg="#cccc00",
                         activeforeground="#324067",
                         activebackground="#cccc00"
                         ).pack(pady=20)

    window.mainloop()




game1=PhotoImage(file="2048.png")
game2=PhotoImage(file="rps.png")


button1 = Button(gameopt,
                 text = "2048",
                 font=("Times New Roman",20),
                 fg = "white",
                 bg = "#293556",
                 activeforeground="white",
                 activebackground="#293556",
                 image= game1,
                 compound="left",
                 command=g_2048)
button1.pack(pady=20)

button2 = Button(gameopt,
                 text = "Rock Paper Scissor",
                 font=("Times New Roman",20),
                 fg = "white",
                 bg = "#293556",
                 activeforeground="white",
                 activebackground="#293556",
                 image=game2,
                 compound="left",
                 command=g_rps
                 )
button2.pack(pady=20)





gameopt.mainloop()