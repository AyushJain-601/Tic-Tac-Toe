from tkinter import *
import itertools
import tkinter.messagebox
 
a=[None]*(3*3)
new=[[None for _ in range(3)] for _ in range(3)]

class button:
    def __init__(self,master):
        self.frme=Frame(master)                 #creating frame
        self.frme.pack()
        self.players=itertools.cycle(["X","O"]) #adding elements
        self.player=next(self.players)          #switiching elements
        self.board()                            #creating board         

    def commnd(self,a,x):
        def on_click():
            #a["text"]=self.player
            a[x].config(text=self.player)
            a[x].config(state="disabled")
            self.player1_won(a)
            self.player2_won(a)
            self.draw(a)
            self.player=next(self.players)
        return on_click
    
    def board(self):
        y=0
        for x in range(0,9):
            #for y in range(0,3):
            a[x]= Button(self.frme,text=" ",width=10,fg="black",height=5,font=('Helvetica', '20'))     #creating buttons
            a[x].grid(row=int(x/3),column=y%3)                                              #aligning them
            y=y+1
            a[x]["command"]=self.commnd(a,x)            #assigning command
    
    
    def player1_won(self,a):                                    #checking winning condition

        y=0 
        for x in range(0,9):
            #for y in range(0,3):
            new[int(x/3)][y%3]=a[x]['text']
            y=y+1
        if(new[0][0]=='X'and new[0][1]=='X' and new[0][2]=='X' or
           new[1][0]=='X'and new[1][1]=='X' and new[1][2]=='X' or
           new[2][0]=='X'and new[2][1]=='X' and new[2][2]=='X' or
           new[0][0]=='X'and new[1][0]=='X' and new[2][0]=='X' or
           new[0][1]=='X'and new[1][1]=='X' and new[2][1]=='X' or
           new[0][2]=='X'and new[1][2]=='X' and new[2][2]=='X' or
           new[0][0]=='X'and new[1][1]=='X' and new[2][2]=='X' or
           new[0][2]=='X'and new[1][1]=='X' and new[2][0]=='X' ) is True:
            tkinter.messagebox.showinfo("GAME OVER!","player {} has won!".format(self.player))   #message pop up window
            self.frme.quit()                                         #closing the game
    
    def player2_won(self,a):
        y=0
        for x in range(0,9):
            #for y in range(0,3):
            new[int(x/3)][y%3]=a[x].cget('text')
            y=y+1
        if(new[0][0]=='O'and new[0][1]=='O' and new[0][2]=='O' or
           new[1][0]=='O'and new[1][1]=='O' and new[1][2]=='O' or
           new[2][0]=='O'and new[2][1]=='O' and new[2][2]=='O' or
           new[0][0]=='O'and new[1][0]=='O' and new[2][0]=='O' or
           new[0][1]=='O'and new[1][1]=='O' and new[2][1]=='O' or
           new[0][2]=='O'and new[1][2]=='O' and new[2][2]=='O' or
           new[0][0]=='O'and new[1][1]=='O' and new[2][2]=='O' or
           new[0][2]=='O'and new[1][1]=='O' and new[2][0]=='O' ) is True:
            tkinter.messagebox.showinfo("GAME OVER!","player {} has won!".format(self.player))
            self.frme.quit()
       
        
    def draw(self,a):
        y=0
        z=0
        for x in range(0,9):
            new[int(x/3)][y%3]=a[x].cget('text')
            y=y+1
        y=0
        for x in range(0,9):
            if (new[int(x/3)][y%3]=='X'or new[int(x/3)][y%3]=='O') is True:
                z=z+1
                y=y+1
        if(z==9) is True:       
            tkinter.messagebox.showinfo("GAME OVER","DRAW")
            self.frme.quit()
root=Tk()
b=button(root)
root.mainloop()
