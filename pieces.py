from board import*
chessBoardImage = [[1] * 8 for i in range(8)]

chess_letter_to_index = {
   "a" : 0,
   "b" : 1,
   "c" : 2,
   "d" : 3,
   "e" : 4,
   "f" : 5,
   "g" : 6,
   "h" : 7
}

chess_index_to_letter = {
   0: "a",
   1: "b",
   2: "c",
   3: "d",
   4: "e",
   5: "f",
   6: "g",
   7: "h"
}

#this function is telling us all the possible places this knight can move given a certain position
class Moves(object):
    def KnightMoves(self, pos, chessBoardImage):
        column = pos.strip().lower()[0]
        row = pos.strip().lower()[1]
        row = int(row) - 1
        column = chess_letter_to_index[column]
        i = row
        j = column
        solutionMoves = []
        
        try:
            temp = chessBoardImage[i + 1][j - 2]
            solutionMoves.append([i + 1, j - 2])
        except:
            pass
        try:
            temp = chessBoardImage[i + 2][j - 1]
            solutionMoves.append([i + 2, j - 1])
        except:
            pass
        try:
            temp = chessBoardImage[i + 2][j + 1]
            solutionMoves.append([i + 2, j + 1])
        except:
            pass
        try:
           temp = chessBoardImage[i + 1][j + 2]
           solutionMoves.append([i + 1, j + 2])
        except:
            pass
        try:
            temp = chessBoardImage[i - 1][j + 2]
            solutionMoves.append([i - 1, j + 2])
        except:
            pass
        try:
            temp = chessBoardImage[i - 2][j + 1]
            solutionMoves.append([i - 2, j + 1])
        except:
            pass
        try:
            temp = chessBoardImage[i - 2][j - 1]
            solutionMoves.append([i - 2, j - 1])
        except:
            pass
        try:
            temp = chessBoardImage[i - 1][j - 2]
            solutionMoves.append([i - 1, j - 2])
        except:
            pass

        #take out negative values
        temp = [move for move in solutionMoves if move[0] >= 0 and move[1] >= 0 and move[1] <=7]
        self.allMoves = ["".join([chess_index_to_letter[move[1]], str(move[0] + 1)]) for move in temp]
        self.allMoves.sort()

    def CastleMoves(self, pos, chessBoardImage):
        column = pos.strip().lower()[0]
        row = pos.strip().lower()[1]
        row = int(row) - 1
        column = chess_letter_to_index[column]
        i = row
        j = column
        solutionMoves = []

        for j in range(8):
            if j != column:
                solutionMoves.append((row, j))

        for i in range(8):
            if i != row:
                solutionMoves.append((i, column))

        self.allMoves = ["".join([chess_index_to_letter[move[1]], str(move[0] + 1)]) for move in solutionMoves]
        self.allMoves.sort()
        return self.allMoves

    def BishopMoves(self, pos, chessBoardImage):
        column = pos.strip().lower()[0]
        row = pos.strip().lower()[1]
        row = int(row) - 1
        number = chess_letter_to_index[column]
        i = row
        j = number
        solutionMoves = []

        #upward right diagonal
        for n in range(9):
            try:
                solutionMoves.append([i + n, j + n])
            except:
                pass

        #upward left diagonal
        for n in range(9):
            try:
                solutionMoves.append([i + n, j - n])
            except:
                pass

       #downward left diagnoal
        for n in range(9):
            try:
                solutionMoves.append([i - n, j - n])
            except:
                pass

       #downward right dia5onal
        for n in range(9):
            try:
                solutionMoves.append([i - n, j + n])
            except:
                pass

        temp = [move for move in solutionMoves if move[0] >= 0 and move[1] >= 0 and move[0] <= 7 and move[1] <= 7]
        #coming from KNIGHT self.allMoves = ["".join([chess_index_to_letter[move[1]], str(move[0] + 1)]) for move in temp]
        self.allBish = ["".join([chess_index_to_letter[move[1]], str(move[0] + 1)]) for move in temp]
        self.allBish.sort()
        return self.allBish

    def QueenMoves(self, pos, chessBoardImage):
        column = pos.strip().lower()[0]
        row = pos.strip().lower()[1]
        row = int(row) - 1
        column = chess_letter_to_index[column]
        i = row
        j = column
        solutionMoves = []

        for n in range(9):
            try:
                solutionMoves.append([i + n, j + n])
            except:
                pass

        #upward left diagonal
        for n in range(9):
            try:
                solutionMoves.append([i + n, j - n])
            except:
                pass

       #downward left diagnoal
        for n in range(9):
            try:
                solutionMoves.append([i - n, j - n])
            except:
                pass

       #downward right dia5onal
        for n in range(9):
            try:
                solutionMoves.append([i - n, j + n])
            except:
                pass

        for j in range(8):
            if j != column:
                solutionMoves.append((row, j))

        for i in range(8):
            if i != row:
                solutionMoves.append((i, column))


        temp = [move for move in solutionMoves if move[0] >= 0 and move[1] >= 0 and move[0] <= 7 and move[1] <= 7]
        self.allMoves = ["".join([chess_index_to_letter[move[1]], str(move[0] + 1)]) for move in temp]
        self.allMoves.sort()
        return self.allMoves


    def KingMoves(self, pos, chessBoardImage):
        column = pos.strip().lower()[0]
        row = pos.strip().lower()[1]
        row = int(row) - 1
        column = chess_letter_to_index[column]
        i = row
        j = column
        solutionMoves = []

        try:
            temp = chessBoardImage[i + 1][j + 1]
            solutionMoves.append([i + 1, j + 1])
        except:
            pass

        try:
            temp = chessBoardImage[i - 1][j - 1]
            solutionMoves.append([i - 1, j - 1])
        except:
            pass

        try:
            temp = chessBoardImage[i + 1][j - 1]
            solutionMoves.append([i + 1, j - 1])
        except:
            pass

        try:
            temp = chessBoardImage[i - 1][j]
            solutionMoves.append([i - 1, j])
        except:
            pass

        try:
            temp = chessBoardImage[i + 1][j]
            solutionMoves.append([i + 1, j])
        except:
            pass

        try:
            temp = chessBoardImage[i][j + 1]
            solutionMoves.append([i, j + 1])
        except:
            pass

        try:
            temp = chessBoardImage[i][j - 1]
            solutionMoves.append([i, j - 1])
        except:
            pass
        
        try:
            temp = chessBoardImage[i - 1][j + 1]
            solutionMoves.append([i - 1, j + 1])
        except:
            pass

        #take out negative values
        temp = [move for move in solutionMoves if move[0] >= 0 and move[1] >= 0]
        self.allKing = ["".join([chess_index_to_letter[move[1]], str(move[0] + 1)]) for move in temp]
        self.allKing.sort()
        return self.allKing
        
    def PawnMoves(self, pos, chessBoardImage):
        column = pos.strip().lower()[0]
        row = pos.strip().lower()[1]
        row = int(row) - 1
        column = chess_letter_to_index[column]
        i = row
        j = column
        solutionMoves = []

        try:
            temp = chessBoardImage[i + 1][j]
            solutionMoves.append([i + 1, j])
        except:
            pass
     
        #take out negative values
        temp = [move for move in solutionMoves if move[0] >= 0 and move[1] >= 0]
        self.allMoves = ["".join([chess_index_to_letter[move[1]], str(move[0] + 1)]) for move in temp]
        attack = [[i+1, j+1], [i+1, j-1]]
        temp2 = [hit for hit in attack if hit[0] >= 0 and hit[1] >= 0]
        self.attackMoves = ["".join([chess_index_to_letter[hit[1]], str(hit[0] + 1)]) for hit in temp2]
        for i in self.attackMoves:
            if legend[i] in player2:
                self.allMoves.append(i)
        self.allMoves.sort()
        print(self.allMoves)
        return self.allMoves

    def PawnMoves2(self, pos, chessBoardImage):
        column = pos.strip().lower()[0]
        row = pos.strip().lower()[1]
        row = int(row) - 1
        column = chess_letter_to_index[column]
        i = row
        j = column
        solutionMoves = []

        try:
            temp = chessBoardImage[i - 1][j]
            solutionMoves.append([i - 1, j])
        except:
            pass

        #take out negative values
        temp = [move for move in solutionMoves if move[0] >= 0 and move[1] >= 0]
        self.allMoves = ["".join([chess_index_to_letter[move[1]], str(move[0] + 1)]) for move in temp]
        attack = [[i-1, j-1], [i-1, j+1]]
        temp2 = [hit for hit in attack if hit[0] >= 0 and hit[1] >= 0]
        self.attackMoves = ["".join([chess_index_to_letter[hit[1]], str(hit[0] + 1)]) for hit in temp2]
        for i in self.attackMoves:
            if legend[i] in player1:
                self.allMoves.append(i)
        self.allMoves.sort()
        print(self.allMoves)
        return self.allMoves
        
    def CheckPlayer2Loss(self):
        self.everymove = []
        for key in point:
            if key == 'P1':
               self.PawnMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)
            if key == 'C1':
               self.PawnMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)
            if key == 'H1':
               self.PawnMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)
            if key == 'B1':
               self.PawnMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)
            if key == 'Q1':
               self.PawnMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)  
            if key == 'K1':
               self.KingMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)  
        for i in self.everymove:
            if i == point['K2']:
                print ('Check! \n')
                return True
                #if any of player 2's pieces allowable moves is where King is sitting,break

    def CheckPlayer1Loss(self):
        self.everymove = []
        for key in point:
            if key == 'P2':
               self.PawnMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)
            if key == 'C2':
               self.PawnMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)
            if key == 'H2':
               self.PawnMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)
            if key == 'B2':
               self.PawnMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)
            if key == 'Q2':
               self.PawnMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)  
            if key == 'K2':
               self.KingMoves(point[key], chessBoard)
               self.everymove.append(self.allMoves)  
        for i in self.everymove:
            if i == point['K1']:
                print ('Check! \n')
                return True

    def CheckMatePlayer2Loss(self):
        self.everymove = []
        self.count = 0
        for key in point:
            if key == 'C1':
               self.CastleMoves(point[key], chessBoard)
               for i in self.allMoves:
                   self.everymove.append(i)
            if key == 'H1':
               self.KnightMoves(point[key], chessBoard)
               for i in self.allMoves:
                    if i not in self.everymove:
                        self.everymove.append(i)
            if key == 'B1':
               self.BishopMoves(point[key], chessBoard)
               for i in self.allBish:
                    if i not in self.everymove:
                        self.everymove.append(i)
            if key == 'P1':
               self.PawnMoves(point[key], chessBoard)
               for i in self.allMoves:
                    if i not in self.everymove:
                        self.everymove.append(i)
            if key == 'Q1':
               self.QueenMoves(point[key], chessBoard)
               for i in self.allMoves:
                    if i not in self.everymove:
                        self.everymove.append(i)
            if key == 'K1':
               self.KingMoves(point[key], chessBoard)
                        
        self.everymove.sort()
        for i in self.allKing:
            for j in self.everymove:
                if i == j:
                    self.count +=1
        if self.count >= len(self.allKing):
            return True

    def CheckMatePlayer1Loss(self):
        self.everymove = []
        self.count = 0
        for key in point:
            if key == 'C2':
               self.CastleMoves(point[key], chessBoard)
               for i in self.allMoves:
                   self.everymove.append(i)
            if key == 'H2':
               self.KnightMoves(point[key], chessBoard)
               for i in self.allMoves:
                    if i not in self.everymove:
                        self.everymove.append(i)
            if key == 'B2':
               self.BishopMoves(point[key], chessBoard)
               for i in self.allBish:
                    if i not in self.everymove:
                        self.everymove.append(i)
            if key == 'P2':
               self.PawnMoves(point[key], chessBoard)
               for i in self.allMoves:
                    if i not in self.everymove:
                        self.everymove.append(i)
            if key == 'Q2':
               self.QueenMoves(point[key], chessBoard)
               for i in self.allMoves:
                    if i not in self.everymove:
                        self.everymove.append(i)
            if key == 'K2':
               self.KingMoves(point[key], chessBoard)
                        
        self.everymove.sort()
        for i in self.allKing:
            for j in self.everymove:
                if i == j:
                    self.count +=1
        if self.count >= len(self.allKing):
            return True

    def ManDown(self):
        pass
            #if any of the pieces get taken

    def PawnAttack(self):
        pass
                #if player2 item is [i+1][j+1] or [i-1][j+1] then append either move to alloves

    def currentMove(self): #before this happens we have to be able to determine if its a player 1 or player 2 item, a way this could be done would be do have it like if the 2nd item in origin is a 2 do this, if a 1 do this.
        if legend[self.origin][2] == '2':
            self.Player2()

        if legend[self.origin][1] == '1':
            self.Player1()
    
    def Player1(self):
        self.origin = input('Where is the piece you want to move? ')
        if self.CheckPlayer1Loss is True:
            while legend[self.origin] != 'K':
                print('You have to move your King! \n')
                self.origin = input('Where would you like to move your king')
         #returning the colour of the board to the appropriate tile

        if legend[self.origin] == 'P1': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.PawnMoves(self.origin, chessBoard)
           self.pos = input('Where would you like to move your pawn? \n')
           while self.pos not in self.allMoves or legend[self.pos] in player1:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your pawn? \n')
        if legend[self.origin] == 'H1': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.KnightMoves(self.origin, chessBoard)
           self.pos = input('Where would you like to move your Knight? \n')
           while self.pos not in self.allMoves or legend[self.pos] in player1:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your Knight? \n')
        if legend[self.origin] == 'Q1': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.QueenMoves(self.origin, chessBoard)
           self.pos = input('Where would you like to move your Queen? \n')
           while self.pos not in self.allMoves or legend[self.pos] in player1:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your Queen? \n')
        if legend[self.origin] == 'B1': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.BishopMoves(self.origin, chessBoard)
           self.pos = input('Where would you like to move your bishop? \n')
           while self.pos not in self.allBish or legend[self.pos] in player1:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your bishop? \n')
        if legend[self.origin] == 'C1': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.CastleMoves(self.origin, chessBoard)
           self.pos = input('Where would you like to move your Castle? \n')
           while self.pos not in self.allMoves or legend[self.pos] in player1:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your Castle? \n')
        if legend[self.origin] == 'K1': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.KingMoves(self.origin, chessBoard)
           self.pos = input('Where would you like to move your King? \n')
           while self.pos not in self.allKing or legend[self.pos] in player1:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your King? \n')
        elif legend[self.origin] not in player1:
            print("\n You must select a piece Player 1! \n")
            s.Player1()

        legend[self.pos] = legend[self.origin]
        point[legend[self.pos]] = self.pos
        legend[self.origin] = actualBoard[self.origin]
        createboard()

    def Player2(self):
        self.origin = input('Where is the piece you want to move? ')
        if self.CheckPlayer2Loss is True:
            while legend[self.origin] != 'K':
                print('You have to move your King! \n')
                self.origin = input('Where would you like to move your king')
        #returning the colour of the board to the appropriate tile

        if legend[self.origin] == 'P2': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.PawnMoves2(self.origin, chessBoard)
           self.pos = input('Where would you like to move your pawn? \n')
           while self.pos not in self.allMoves or legend[self.pos] in player2:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your pawn? \n')
        if legend[self.origin] == 'H2': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.KnightMoves(self.origin, chessBoard)
           self.pos = input('Where would you like to move your Knight? \n')
           while self.pos not in self.allMoves or legend[self.pos] in player2:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your Knight? \n')
        if legend[self.origin] == 'Q2': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.QueenMoves(self.origin, chessBoard)
           self.pos = input('Where would you like to move your Queen? \n')
           while self.pos not in self.allMoves or legend[self.pos] in player2:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your Queen? \n')
        if legend[self.origin] == 'B2': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.BishopMoves(self.origin, chessBoard)
           self.pos = input('Where would you like to move your bishop? \n')
           while self.pos not in self.allBish or legend[self.pos] in player2:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your bishop? \n')
        if legend[self.origin] == 'C2': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.CastleMoves(self.origin, chessBoard)
           self.pos = input('Where would you like to move your Castle? \n')
           while self.pos not in self.allMoves or legend[self.pos] in player2:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your Castle? \n')
        if legend[self.origin] == 'K2': #or pawn2 or pawn 3... this will move every piece to its new position and will provide the allowable positions
           self.KingMoves(self.origin, chessBoard)
           self.pos = input('Where would you like to move your King? \n')
           while self.pos not in self.allKing or legend[self.pos] in player2:
               print ('That is an illegal move, please try again \n')
               self.pos = input('Where would you like to move your King? \n')

        elif legend[self.origin] not in player2:
            print("\n You must select a piece Player 2! \n")
            s.Player2()  
        
        legend[self.pos] = legend[self.origin]
        point[legend[self.pos]] = self.pos
        legend[self.origin] = actualBoard[self.origin]
        createboard()


    """def Movement(self):
        self.origin = input('Where is the piece you want to move? ')
        if self.Check is True:
            while legend[self.origin] != 'K':
                print('You have to move your King! \n')
                self.origin = input('Where would you like to move your king')
        self.FriendlyFire()
        legend[self.pos] = legend[self.origin]
        point[legend[self.pos]] = self.pos
        legend[self.origin] = actualBoard[self.origin] #returning the colour of the board to the appropriate tile
        createboard()"""
        #self.Check()
        
#for soem reason I'm getting an error with my bishop movement... ive replaced the tiles with black adn white when they move though.
initialize_Board()
s = Moves()
def run():
    count = 0
    while count < 1000000:
        print('\nYour move player 1 \n')
        s.Player1()
        s.CheckMatePlayer2Loss()
        count= count + 1
        if s.CheckMatePlayer2Loss() is True:
            print('Checkmate Game Over, Player 1 Wins!')
            break
        print('\n Your move player 2 \n')
        s.Player2()
        count= count + 1
        if s.CheckMatePlayer1Loss() is True:
            print('Checkmate Game Over, Player 2 Wins!')
            break

run()

#check and checkmate needs to be analyzed after every move not after both sequences are done so the s.checkmate needs to be somewhere else.. in the movement, and then movement needs to alternate between player 1 and 2
