import pygame

class TicTacToe:
    def __init__(self):
        #creates the window
        pygame.init()
        
        #specifies the width and height
        self.width=600
        self.height=600

        #defines variables
        self.winner_text=""
        self.game_full=False
        self.player_turn="X"
        self.run=True

        #displays the window with its specified width and height
        self.window=pygame.display.set_mode((self.width, self.height))

        #sets the caption 
        pygame.display.set_caption("Tic Tac Toe")

        #creates a board that stores input(X or O)
        self.board=[["", "", ""],
                    ["", "", ""],
                    ["", "", ""]]
        
    
    def drawlines(self):
        #draws vertical lines
        self.verticalline1=pygame.draw.line(self.window, (0, 0, 0), (200, 50), (200, 550), 10)
        self.verticalline2=pygame.draw.line(self.window, (0, 0, 0), (400, 50), (400, 550), 10)

        #draws horizontal lines
        self.horizontalline1=pygame.draw.line(self.window, (0,0, 0), (50, 200), (550, 200), 10)
        self.horizontalline2=pygame.draw.line(self.window, (0,0, 0), (50, 400), (550, 400), 10)
    def drawshapes(self):
        #goes through each square in board and checks if X or O is in it then displays it in that area on the screen
        for self.row in range(3):
            for self.column in range(3):
                if self.board[self.row][self.column]=="X":
                    self.X=self.font1.render("X", False, (128, 0, 128))
                    self.window.blit(self.X, (self.column*200+50, self.row*200+50))
                elif self.board[self.row][self.column]=="O":
                    self.O=self.font1.render("O", False, (128, 0, 128))
                    self.window.blit(self.O, (self.column*200+50, self.row*200+50))

    def reset_game(self):
        #resets the variables
        self.board=[["", "", ""], ["", "", ""], ["", "", ""]]
        self.player_turn="X"
        self.game_active=True
        self.winner_text=None

    def checkgame_full(self):
        #goes through every area and checks if empty and returns false(not full) if not returns true(full)
        for row in range(3):
            for column in range(3):
                if self.board[row][column]=="":
                    return False
                        
        return True
            


    def run_game(self):
        self.game_active=True
        #creates two fonts
        self.font1=pygame.font.Font(None, 150)
        self.font2=pygame.font.Font(None, 50)

        #mainloop
        while self.run:

            #goes through each event done by user 
            for event in pygame.event.get():

                #checks if user exits the window
                if event.type==pygame.QUIT:
                    self.run=False
                #checks if user presses on a key and checks if that key was space an resets if true
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        self.reset_game()
                #checks if user presses onto the screen then takes the position at x and y
                if event.type==pygame.MOUSEBUTTONDOWN:
                    self.x,self.y=event=event.pos
                    self.row=self.y//200
                    self.column=self.x//200
                    #checks if position is empty in board
                    if self.board[self.row][self.column]=="":
                        self.board[self.row][self.column]=self.player_turn
                        #checks which player has the turn then alternates to the other player
                        if self.player_turn=="X":
                            self.player_turn="O"
                        else:
                            self.player_turn="X"
            #checks if game is active
            if self.game_active:
                
                #fills the screen with a color
                self.window.fill((0, 0, 82))  #alternate color: (162,228,184)

                #draws lines and shapes
                self.drawlines()
                self.drawshapes()

                #checks if X or O wins
                if self.board[0][0]=="X" and self.board[0][1]=="X" and self.board[0][2]=="X":
                    self.winner_text="X wins"
                    self.game_active=False
                elif self.board[1][0]=="X" and self.board[1][1]=="X" and self.board[1][2]=="X":
                    self.winner_text="X wins"
                    self.game_active=False
                elif self.board[2][0]=="X" and self.board[2][1]=="X" and self.board[2][2]=="X":
                    self.winner_text="X wins"
                    self.game_active=False
                elif self.board[0][0]=="X" and self.board[1][1]=="X" and self.board[2][2]=="X":
                    self.winner_text="X wins"
                    self.game_active=False
                elif self.board[0][2]=="X" and self.board[1][1]=="X" and self.board[2][0]=="X":
                    self.winner_text="X wins"
                    self.game_active=False
                elif self.board[0][0]=="X" and self.board[1][0]=="X" and self.board[2][0]=="X":
                    self.winner_text="X wins"
                    self.game_active=False
                elif self.board[0][1]=="X" and self.board[1][1]=="X" and self.board[2][1]=="X":
                    self.winner_text="X wins"
                    self.game_active=False
                elif self.board[0][2]=="X" and self.board[1][2]=="X" and self.board[2][2]=="X":
                    self.winner_text="X wins"
                    self.game_active=False
                elif self.board[0][0]=="O" and self.board[0][1]=="O" and self.board[0][2]=="O":
                    self.winner_text="O wins"
                    self.game_active=False
                elif self.board[1][0]=="O" and self.board[1][1]=="O" and self.board[1][2]=="O":
                    self.winner_text="O wins"
                    self.game_active=False
                elif self.board[2][0]=="O" and self.board[2][1]=="O" and self.board[2][2]=="O":
                    self.winner_text="O wins"
                    self.game_active=False
                elif self.board[0][0]=="O" and self.board[1][1]=="O" and self.board[2][2]=="O":
                    self.winner_text="O wins"
                    self.game_active=False
                elif self.board[0][2]=="O" and self.board[1][1]=="O" and self.board[2][0]=="O":
                    self.winner_text="O wins"
                    self.game_active=False
                elif self.board[0][0]=="O" and self.board[1][0]=="O" and self.board[2][0]=="O":
                    self.winner_text="O wins"
                    self.game_active=False
                elif self.board[0][1]=="O" and self.board[1][1]=="O" and self.board[2][1]=="O":
                    self.winner_text="O wins"
                    self.game_active=False
                elif self.board[0][2]=="O" and self.board[1][2]=="O" and self.board[2][2]=="O":
                    self.winner_text="O wins"
                    self.game_active=False
                if self.checkgame_full() and not(self.winner_text=="O wins" or self.winner_text=="X wins"):
                    self.winner_text="Draw"
                    self.game_active=False



                        
            else:
                #fills the winner or draw screen and displays texts onto the screen when game is not active
                self.window.fill((173, 216, 230))
                self.display_winner=self.font1.render(self.winner_text, False, (0, 0, 0))
                self.display_winner_rect=self.display_winner.get_rect(center=(300, 300))
                self.window.blit(self.display_winner, self.display_winner_rect)
                self.press_space=self.font2.render("Press Space to play again", False, (0, 0, 0))
                self.press_space_rect=self.press_space.get_rect(center=(300, 500))
                self.window.blit(self.press_space, self.press_space_rect)
                
            
        
            
            
                
            #updates variables
            pygame.display.update()
        
        #quits the application when its not running
        pygame.quit()

#calls class
game=TicTacToe()

#calls the run function
game.run_game()


        
