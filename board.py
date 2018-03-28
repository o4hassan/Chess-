chessBoard = [['B', '|', 'W', '|'] * 25 for i in range(8)]

def createboard():
    print(chessBoard[0][1], legend['a8'], chessBoard[0][3], legend['b8'], chessBoard[0][5], legend['c8'], chessBoard[0][7], legend['d8'], chessBoard[0][9], legend['e8'], chessBoard[0][11], legend['f8'], chessBoard[0][13], legend['g8'], chessBoard[0][15], legend['h8'], chessBoard[0][17])
    print ('---------------------------------')
    print('|', legend['a7'], chessBoard[1][1], legend['b7'], chessBoard[1][3], legend['c7'], chessBoard[1][5], legend['d7'], chessBoard[1][7], legend['e7'], chessBoard[1][9], legend['f7'], chessBoard[1][11], legend['g7'], chessBoard[0][13], legend['h7'], chessBoard[0][15])
    print ('---------------------------------')
    print(chessBoard[2][1], legend['a6'], chessBoard[2][3], legend['b6'], chessBoard[2][5], legend['c6'], chessBoard[2][7], legend['d6'], chessBoard[2][9], legend['e6'], chessBoard[2][11], legend['f6'], chessBoard[2][13], legend['g6'], chessBoard[2][15], legend['h6'], chessBoard[0][17])
    print ('---------------------------------')
    print('|', legend['a5'], chessBoard[3][1], legend['b5'], chessBoard[3][3], legend['c5'], chessBoard[3][5], legend['d5'], chessBoard[3][7], legend['e5'], chessBoard[3][9], legend['f5'], chessBoard[3][11], legend['g5'], chessBoard[3][13], legend['h5'], chessBoard[0][15])
    print ('---------------------------------')
    print(chessBoard[4][1], legend['a4'], chessBoard[4][3], legend['b4'], chessBoard[4][5], legend['c4'], chessBoard[4][7], legend['d4'], chessBoard[4][9], legend['e4'], chessBoard[4][11], legend['f4'], chessBoard[4][13], legend['g4'], chessBoard[4][15], legend['h4'], chessBoard[0][17])
    print ('---------------------------------')
    print('|', legend['a3'], chessBoard[5][1], legend['b3'], chessBoard[5][3], legend['c3'], chessBoard[5][5], legend['d3'], chessBoard[5][7], legend['e3'], chessBoard[5][9], legend['f3'], chessBoard[5][11], legend['g3'], chessBoard[5][13], legend['h3'], chessBoard[0][15])
    print ('---------------------------------')
    print(chessBoard[6][1], legend['a2'], chessBoard[6][3], legend['b2'], chessBoard[6][5], legend['c2'], chessBoard[6][7], legend['d2'], chessBoard[6][9], legend['e2'], chessBoard[6][11], legend['f2'], chessBoard[6][13], legend['g2'], chessBoard[6][15], legend['h2'], chessBoard[0][17])
    print ('---------------------------------')
    print('|', legend['a1'], chessBoard[7][1], legend['b1'], chessBoard[7][3], legend['c1'], chessBoard[7][5], legend['d1'], chessBoard[7][7], legend['e1'], chessBoard[7][9], legend['f1'], chessBoard[7][11], legend['g1'], chessBoard[7][13], legend['h1'], chessBoard[0][15])


player1 = ['P1', 'B1', 'H1', 'C1', 'K1', 'Q1']
player2 = ['P2', 'B2', 'H2', 'C2', 'K2', 'Q2']

legend= {
    'a1':'O',
    'b1':'W',
    'c1':'O',
    'd1':'W',
    'e1':'O',
    'f1':'W',
    'g1':'O',
    'h1':'W',
    'a2':'W',
    'b2':'O',
    'c2':'W',
    'd2':'O',
    'e2':'W',
    'f2':'O',
    'g2':'W',
    'h2':'O',
    'a3':'O',
    'b3':'W',
    'c3':'O',
    'd3':'W',
    'e3':'O',
    'f3':'W',
    'g3':'O',
    'h3':'W',
    'a4':'W',
    'b4':'O',
    'c4':'W',
    'd4':'O',
    'e4':'W',
    'f4':'O',
    'g4':'W',
    'h4':'O',
    'a5':'O',
    'b5':'W',
    'c5':'O',
    'd5':'W',
    'e5':'O',
    'f5':'W',
    'g5':'O',
    'h5':'W',
    'a6':'W',
    'b6':'O',
    'c6':'W',
    'd6':'O',
    'e6':'W',
    'f6':'O',
    'g6':'W',
    'h6':'O',
    'a7':'O',
    'b7':'W',
    'c7':'O',
    'd7':'W',
    'e7':'O',
    'f7':'W',
    'g7':'O',
    'h7':'W',
    'a8':'W',
    'b8':'O',
    'c8':'W',
    'd8':'O',
    'e8':'W',
    'f8':'O',
    'g8':'W',
    'h8':'O'
    } #has the board itself, like the white/black pieces - need a way to show this in a cleaner method

def initialize_Board():
    legend['a2'] = 'P1'
    legend['b2'] = 'P1'
    legend['c2'] = 'P1'
    legend['d2'] = 'P1'
    legend['e2'] = 'P1'
    legend['f2'] = 'P1'
    legend['g2'] = 'P1'
    legend['h2'] = 'P1'
    legend['a1'] = 'C1'
    legend['b1'] = 'H1'
    legend['c1'] = 'B1'
    legend['d1'] = 'Q1'
    legend['e1'] = 'K1'
    legend['f1'] = 'B1'
    legend['g1'] = 'H1'
    legend['h1'] = 'C1'
    legend['a7'] = 'P2'
    legend['b7'] = 'P2'
    legend['c7'] = 'P2'
    legend['d7'] = 'P2'
    legend['e7'] = 'P2'
    legend['f7'] = 'P2'
    legend['g7'] = 'P2'
    legend['h7'] = 'P2'
    legend['a8'] = 'C2'
    legend['b8'] = 'H2'
    legend['c8'] = 'B2'
    legend['d8'] = 'Q2'
    legend['e8'] = 'K2'
    legend['f8'] = 'B2'
    legend['g8'] = 'H2'
    legend['h8'] = 'C2'
    createboard()


point = {
    'P1': 'a2',
    'P1': 'b2',
    'P1': 'c2',
    'P1': 'd2',
    'P1': 'e2',
    'P1': 'f2',
    'P1': 'g2',
    'C1': 'a1',
    'H1': 'b1',
    'B1': 'c1',
    'Q1': 'd1',
    'K1': 'e1',
    'B1': 'f1',
    'H1': 'g1',
    'C1': 'h1',
    'P2': 'a2',
    'P2': 'b2',
    'P2': 'c2',
    'P2': 'd2',
    'P2': 'e2',
    'P2': 'f2',
    'P2': 'g2',
    'C2': 'a1',
    'H2': 'b1',
    'B2': 'c1',
    'Q2': 'd1',
    'K2': 'e1',
    'B2': 'f1',
    'H2': 'g1',
    'C2': 'h1'
    }
    
actualBoard= {
    'a1':'O',
    'b1':'W',
    'c1':'O',
    'd1':'W',
    'e1':'O',
    'f1':'W',
    'g1':'O',
    'h1':'W',
    'a2':'W',
    'b2':'O',
    'c2':'W',
    'd2':'O',
    'e2':'W',
    'f2':'O',
    'g2':'W',
    'h2':'O',
    'a3':'O',
    'b3':'W',
    'c3':'O',
    'd3':'W',
    'e3':'O',
    'f3':'W',
    'g3':'O',
    'h3':'W',
    'a4':'W',
    'b4':'O',
    'c4':'W',
    'd4':'O',
    'e4':'W',
    'f4':'O',
    'g4':'W',
    'h4':'O',
    'a5':'O',
    'b5':'W',
    'c5':'O',
    'd5':'W',
    'e5':'O',
    'f5':'W',
    'g5':'O',
    'h5':'W',
    'a6':'W',
    'b6':'O',
    'c6':'W',
    'd6':'O',
    'e6':'W',
    'f6':'O',
    'g6':'W',
    'h6':'O',
    'a7':'O',
    'b7':'W',
    'c7':'O',
    'd7':'W',
    'e7':'O',
    'f7':'W',
    'g7':'O',
    'h7':'W',
    'a8':'W',
    'b8':'O',
    'c8':'W',
    'd8':'O',
    'e8':'W',
    'f8':'O',
    'g8':'W',
    'h8':'O'
    }

"""1P1=legend['a2']
1P2=legend['b2']
1P3=legend['c2']
1P4=legend['d2']
1P5=legend['e2']
1P6=legend['f2']
1P7=legend['g2']
1P8=legend['h2']
1C1=legend['a1']
1K1=legend['b1']
1B1=legend['c1']
1Q=legend['d1']
1KI=legend['e1']
1B2=legend['f1']
1K2=legend['g1']'
1C2=1C3legend['h1']
2P1=legend['a7']
2P2=legend['b7']
2P3=legend['c7']
2P4=legend['d7']
2P5=legend['e7']
2P6=legend['f7']
2P7=legend['g7']
2P8=legend['h7']
2C1=legend['a8']
2K1=legend['b8']
2B1=legend['c8']
2Q=legend['d8']
2KI=legend['e8']
2B1=legend['f8']
2K2=legend['g8']
2C2=legend['h8']



def initialize_Board():
    legend['a2'] = '1P1'
    legend['b2'] = '1P2'
    legend['c2'] = '1P3'
    legend['d2'] = '1P4'
    legend['e2'] = '1P5'
    legend['f2'] = '1P6'
    legend['g2'] = '1P7'
    legend['h2'] = '1P8'
    legend['a1'] = '1C1'
    legend['b1'] = '1K1'
    legend['c1'] = '1B1'
    legend['d1'] = '1Q'
    legend['e1'] = '1KI'
    legend['f1'] = '1B2'
    legend['g1'] = '1K2'
    legend['h1'] = '1C2'
    legend['a7'] = '2P1'
    legend['b7'] = '2P2'
    legend['c7'] = '2P3'
    legend['d7'] = '2P4'
    legend['e7'] = '2P5'
    legend['f7'] = '2P6'
    legend['g7'] = '2P7'
    legend['h7'] = '2P8'
    legend['a8'] = '2C1'
    legend['b8'] = '2K1'
    legend['c8'] = '2B1'
    legend['d8'] = '2Q'
    legend['e8'] = '2KI'
    legend['f8'] = '2B1'
    legend['g8'] = '2K2'
    legend['h8'] = '2C2'
"""


"""
def initialize_Board(): #simulation of a checkmate use this to confirm if checkmate works or not
    legend['a6'] = 'C1'
    legend['b4'] = 'K'
    legend['d2'] = 'H1'
    legend['e2'] = 'H2'
    legend['g3'] = 'B1'
    legend['d7'] = 'B2'
    legend['d3'] = 'C2'
    createboard()


point = { #for checkmate simulation
    'C1': 'a6',
    'H1': 'd2',
    'B1': 'g3',
    'B2': 'd7',
    'H2': 'e2',
    'C2': 'd3',
    'K': 'b4'
    }

"""
