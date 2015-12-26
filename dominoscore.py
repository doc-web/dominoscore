#Domino Score Keeper Application
#Drew Weber
#8.30.15
#v1.0
#
#--------------------------------------------------------------------------
#
#Features:
#   Keeps score for two players
#   Buttons to increment scores by 5, 10, 15, and 20 points
#   Button to reset scores
#   Button to quit application

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        #initialize Frame variable
        tk.Frame.__init__(self, master)
        
        #prepard frame before putting widgets on
        self.pack()
        
        #call to method, make widgets on screen
        self.createWidgets()

    def createWidgets(self):
            #PLAYER 1 Setup
            self.p1Title = tk.Label(self, text="Player 1")
            self.p1Title.grid(row=0, column=0)
            self.p1Score = 0
            self.p1StringVar = tk.StringVar()
            #label will hold score
            self.p1ScoreLabel= tk.Label(self, textvariable=self.p1StringVar)
            #set label to p1 score
            self.p1StringVar.set(self.p1Score)
            #place label on screen
            self.p1ScoreLabel.grid(row=1, column=0)
            #score +5 button
            self.p1_score5_button = tk.Button(self, text="5", command=self.p1_score5)
            self.p1_score5_button.grid(row=2, column=0)
            #score +10 button
            self.p1_score10_button = tk.Button(self, text="10", command=self.p1_score10)
            self.p1_score10_button.grid(row=3, column=0)
            #score +15 button
            self.p1_score15_button = tk.Button(self, text="15", command=self.p1_score15)
            self.p1_score15_button.grid(row=4, column=0)
            #score +20 button
            self.p1_score20_button = tk.Button(self, text="20", command=self.p1_score20)
            self.p1_score20_button.grid(row=5, column=0)
            

            #PLAYER 2 Setup
            self.p2Title = tk.Label(self, text="Player 2")
            self.p2Title.grid(row=0, column=1)
            self.p2Score = 0
            self.p2StringVar = tk.StringVar()
            #label will hold score
            self.p2ScoreLabel= tk.Label(self, textvariable=self.p2StringVar)
            #set label to p2 score
            self.p2StringVar.set(self.p2Score)
            #place label on screen
            self.p2ScoreLabel.grid(row=1, column=1)
            #score +5 button
            self.p2_score5_button = tk.Button(self, text="5", command=self.p2_score5)
            self.p2_score5_button.grid(row=2, column=1)
            #score +10 button
            self.p2_score10_button = tk.Button(self, text="10", command=self.p2_score10)
            self.p2_score10_button.grid(row=3, column=1)
            #score +15 button
            self.p2_score15_button = tk.Button(self, text="15", command=self.p2_score15)
            self.p2_score15_button.grid(row=4, column=1)
            #score +20 button
            self.p2_score20_button = tk.Button(self, text="20", command=self.p2_score20)
            self.p2_score20_button.grid(row=5, column=1)

            #button for resetting scores
            self.RESET = tk.Button(self, text="Reset", command=self.reset_scores)
            self.RESET.grid(row=6, column=0)


            #make button variable for quitting
            self.QUIT = tk.Button(self, text="QUIT", fg="red",bg="black",
                                                command=root.destroy)
            self.QUIT.grid(row=6, column=1)


        
#---------------------------------------------------------------------------        
#PLAYER 1 METHODS-----------------------------------------------------------

    #method to update player one score 5 pts
    def p1_score5(self):
        self.p1Score += 5
        self.p1StringVar.set(self.p1Score)
        
    #method to update player one score 10 pts
    def p1_score10(self):
        self.p1Score += 10
        self.p1StringVar.set(self.p1Score)

    #method to update player one score 15 pts
    def p1_score15(self):
        self.p1Score += 15
        self.p1StringVar.set(self.p1Score)

    #method to update player one score 20 pts
    def p1_score20(self):
        self.p1Score += 20
        self.p1StringVar.set(self.p1Score)

#---------------------------------------------------------------------------        
#PLAYER 2 METHODS-----------------------------------------------------------

    #method to update player two score 5 pts
    def p2_score5(self):
        self.p2Score += 5
        self.p2StringVar.set(self.p2Score)

    #method to update player two score 10 pts
    def p2_score10(self):
        self.p2Score += 10
        self.p2StringVar.set(self.p2Score)

    #method to update player two score 15 pts
    def p2_score15(self):
        self.p2Score += 15
        self.p2StringVar.set(self.p2Score)

    #method to update player two score 20 pts
    def p2_score20(self):
        self.p2Score += 20
        self.p2StringVar.set(self.p2Score)
        
#---------------------------------------------------------------------------         
#AUX Methods----------------------------------------------------------------

    #method to reset scores
    def reset_scores(self):
        #player 1
        self.p1Score = 0
        self.p1StringVar.set(self.p1Score)
        #player 2
        self.p2Score = 0
        self.p2StringVar.set(self.p2Score)
        
#---------------------------------------------------------------------------        
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()

