def isvalidchessboard(**chess):
    num=[1,2,3,4,5,6,7,8]
    letters= ['a','b','c','d','e','f','g','h']
    color= ['b','w']
    check= []
    
    members= ['pawn','bishop','rook','knight','king', 'queen', ]
    try:
        for val in chess.values():
            check.append(val)
       
        if check.count('bpawn')>8 or check.count('wpawn')>8:
            print("Invalid number of pawns, both black and white")
        if check.count('bbishop')>2 or check.count('wbishop')>2:
            print("Invalid number of bishops, both black and white")
        if check.count('brook')>2 or check.count('wrook')>2:
            print("Invalid number of rooks, both black and white")
        if check.count('bking')>1 or check.count('bqueen')>1 or check.count('wking')>1 or check.count('wqueen')>1:
            print("Invalid number of kings and queens")
       
        if check.count('bknight')>2 or check.count('wknight')>2:
            print("Invalid number of knights, both black and white")
       
      

        for key in chess.keys():

            if (int(key[0]) not in num) or (key[1] not in letters):
                print("Invalid position")
            else:
                print("Positions are correct")
        for value in chess.values():
            if value[0] not in color:
                print("Invalid color of player it must be b or w")
            if value[1:] not in members:
                print("Invalid chess piece")
        
    except:
        print("Setup is correct")
    
    
chess= {'1h': 'bking', '6c': 'wqueen'}
isvalidchessboard(**chess)
