import sys
import copy

#Making sure input is correct
error = False
if len(sys.argv) == 4:
    error = False
else:
    error = True

if error == True:
    print("ERROR: Not enough/too many/illegal input arguments.")
    exit()
if sys.argv[1] == '1' or sys.argv[1] == '2':
    error = False
else:
    error = True   
if sys.argv[2] == 'x' or sys.argv[2] == 'X' or sys.argv[2] == 'o' or sys.argv[2] == 'O':
    error = False
else:
    error = True   
if sys.argv[3] == '1' or sys.argv[3] == '2':
    error = False
else:
    error = True   

if error == True:
    print("ERROR: Not enough/too many/illegal input arguments.")
    exit()




class State:
    def __init__(self,board,turn):
        self.board = board
        self.turn = turn

#Setting count to just root node
count = 1

#Making sure that whether you input capital O or non capital o or x in console, the program will still run
if sys.argv[2] == 'o' or sys.argv[2] == 'O':
    initialPlayer = 'o'
elif sys.argv[2] == 'x' or sys.argv[2] == 'X':
    initialPlayer = 'x'

def movesNext(state):
    # movesNext(ToMove in the pseudocode) takes a state and outputs which player will be playing the next move, returns x or o
    if state.turn == 'x':
        return 'x'
    elif state.turn == 'o':
        return 'o'

def actions(state):
    #actions returns the possible actions based on the given game board
    #For each value that is null, record the index of that value and as such the indexes are the empty squares (actions we can take)
    
    possibleActions = [] #Initialize the empty list of actions
    for i in range(9):
        if state.board[i] == None:
            correct = i + 1
            possibleActions.append(correct)

    return possibleActions

def isTerminal(state):
    # isTerminal takes a state and decides whether it is in terminal state or not, returns true/false
    #Terminal state is when there is either 3 x's or 3 o's in a row horizontally, vertically, and diagonally, or when we have run out of actions 
    #For when there are 3 x or os horizontally:
    numofActions = actions(state)
    if (state.board[0] == 'x' and state.board[1] == 'x' and state.board[2] == 'x') or (state.board[0] == 'o' and state.board[1] == 'o' and state.board[2] == 'o'):
        return True
    elif (state.board[3] == 'x' and state.board[4] == 'x' and state.board[5] == 'x') or (state.board[3] == 'o' and state.board[4] == 'o' and state.board[5] == 'o'):
        return True
    elif (state.board[6] == 'x' and state.board[7] == 'x' and state.board[8] == 'x') or (state.board[6] == 'o' and state.board[7] == 'o' and state.board[8] == 'o'):
        return True
    #For when there are 3 x or os vertically:
    elif (state.board[0] == 'x' and state.board[3] == 'x' and state.board[6] == 'x') or (state.board[0] == 'o' and state.board[3] == 'o' and state.board[6] == 'o'):
        return True
    elif (state.board[1] == 'x' and state.board[4] == 'x' and state.board[7] == 'x') or (state.board[1] == 'o' and state.board[4] == 'o' and state.board[7] == 'o'):
        return True
    elif (state.board[2] == 'x' and state.board[5] == 'x' and state.board[8] == 'x') or (state.board[2] == 'o' and state.board[5] == 'o' and state.board[8] == 'o'):
        return True
    #For when there are 3 x or os diagonally
    elif (state.board[0] == 'x' and state.board[4] == 'x' and state.board[8] == 'x') or (state.board[0] == 'o' and state.board[4] == 'o' and state.board[8] == 'o'):
        return True
    elif (state.board[2] == 'x' and state.board[4] == 'x' and state.board[6] == 'x') or (state.board[2] == 'o' and state.board[4] == 'o' and state.board[6] == 'o'):
        return True
    #For when there are no actions remaining
    elif (numofActions) == []:
        return True
    else:
        return False
    
def result(state, action):
    # returns the game board after the given action has been applied
    listnum = action - 1
    
    stateCont = copy.deepcopy(state) #Make a duplicate of the original state
    #if player is x, input x. If player is o, input o.
    player = movesNext(state)
    if player == 'x':
        stateCont.board[listnum] = 'x' 
    else:
        stateCont.board[listnum] = 'o'
    
    return stateCont

def utility(state,player):
    #Utility calculates the terminal state utility of a game board
    #print(state.board,player)
    #player = state.turn 
    #Is it supposed to calculate utility based on the initialPlayer?
    
    #If the player is x, calculate utility
    if player == 'x':
        #All win cases for x
        #Vertical
        if (state.board[0] == 'x' and state.board[1] == 'x' and state.board[2] == 'x'):
            return 1
        elif (state.board[3] == 'x' and state.board[4] == 'x' and state.board[5] == 'x'):
            return 1
        elif (state.board[6] == 'x' and state.board[7] == 'x' and state.board[8] == 'x'):
            return 1
        #Horizontal
        elif (state.board[0] == 'x' and state.board[3] == 'x' and state.board[6] == 'x'):
            return 1
        elif (state.board[1] == 'x' and state.board[4] == 'x' and state.board[7] == 'x'):
            return 1
        elif (state.board[2] == 'x' and state.board[5] == 'x' and state.board[8] == 'x'):
            return 1
        #Diagonal
        elif (state.board[0] == 'x' and state.board[4] == 'x' and state.board[8] == 'x'):
            return 1
        elif (state.board[2] == 'x' and state.board[4] == 'x' and state.board[6] == 'x'):
            return 1
        #All lose cases for x
        #Horizontal
        elif (state.board[0] == 'o' and state.board[1] == 'o' and state.board[2] == 'o'):
            return -1
        elif (state.board[3] == 'o' and state.board[4] == 'o' and state.board[5] == 'o'):
            return -1
        elif (state.board[6] == 'o' and state.board[7] == 'o' and state.board[8] == 'o'):
            return -1
        #Vertical
        elif (state.board[0] == 'o' and state.board[3] == 'o' and state.board[6] == 'o'):
            return -1
        elif (state.board[1] == 'o' and state.board[4] == 'o' and state.board[7] == 'o'):
            return -1
        elif (state.board[2] == 'o' and state.board[5] == 'o' and state.board[8] == 'o'):
            return -1
        #Diagonal
        elif (state.board[0] == 'o' and state.board[4] == 'o' and state.board[8] == 'o'):
            return -1
        elif (state.board[2] == 'o' and state.board[4] == 'o' and state.board[6] == 'o'):
            return -1
        #Tie
        else:
            return 0
    elif player == 'o':
        #Same with x player, just flipped
        #All loss cases for o
        #Horizontal
        if (state.board[0] == 'x'and state.board[1] == 'x'and state.board[2] == 'x'):
            return -1
        elif (state.board[3] == 'x'and state.board[4] == 'x' and state.board[5] == 'x'):
            return -1
        elif (state.board[6] == 'x' and state.board[7] == 'x' and state.board[8] == 'x'):
            return -1
        #Vertical
        elif (state.board[0] == 'x' and state.board[3] == 'x' and state.board[6] == 'x'):
            return -1
        elif (state.board[1] == 'x' and state.board[4] == 'x' and state.board[7] == 'x'):
            return -1
        elif (state.board[2] == 'x' and state.board[5] == 'x' and state.board[8] == 'x'):
            return -1
        #Diagonal
        elif (state.board[0] == 'x' and state.board[4] == 'x' and state.board[8] == 'x'):
            return -1
        elif (state.board[2]== 'x' and state.board[4] == 'x' and state.board[6] == 'x'):
            return -1
        #All win cases for o
        #Horizontal
        elif (state.board[0] == 'o' and state.board[1] == 'o' and state.board[2] == 'o'):
            return 1
        elif (state.board[3] == 'o' and state.board[4] == 'o' and state.board[5] == 'o'):
            return 1
        elif (state.board[6] == 'o' and state.board[7] == 'o' and state.board[8] == 'o'):
            return 1
        #Vertical
        elif (state.board[0] == 'o' and state.board[3] == 'o' and state.board[6] == 'o'):
            return 1
        elif (state.board[1] == 'o' and state.board[4] == 'o' and state.board[7] == 'o'):
            return 1
        elif (state.board[2] == 'o' and state.board[5] == 'o' and state.board[8] == 'o'):
            return 1
        #Diagonal
        elif (state.board[0] == 'o' and state.board[4] == 'o' and state.board[8] == 'o'):
            return 1
        elif (state.board[2] == 'o' and state.board[4] == 'o' and state.board[6] == 'o'):
            return 1
        #Tie
        else:
            return 0
    else:
        print("Mistake?")

def minimaxSearch(state):
    player = movesNext(state) #Initial player is set
  
    valMoveTuple = minValue(state)
    value = valMoveTuple[0] #Utility from minValue is stored here
    move = valMoveTuple[1] #Move from minValue is stored here
    return move

def minimaxSearch2(state):
    #This is for computer 2
    player = movesNext(state) #Initial player is set
  
    valMoveTuple = maxValue(state)
    value = valMoveTuple[0] #Utility from maxValue is stored here
    move = valMoveTuple[1] #Move from maxValue is stored here
    return move

def maxValue(state):   
    player = movesNext(state) #The player is decided based on movesNext, which returns state.turn
    
    if player == 'x':  # Switching to the next player, from x to o or from o to x
        state.turn = 'o'
    elif player == 'o':
        state.turn = 'x'

    if isTerminal(state): 
        util = utility(state,initialPlayer) #If the state is terminal, then calculate the utility of the state based on the initial player
        return util, None # Return the utility and the move(which is none because there is no more moves)
    
    v = float('-inf')

    for a in actions(state): #For each possible action,  calculate what the state will look like given action a, Then run minValue on that state
        resul = result(state,a)
        global count
        count = count + 1
        thetuple = minValue(resul)
        
        v2 = thetuple[0] # Store the utility from minValue to v2
        a2 = thetuple[1] #Store the move from minValue to a2
        if v2 > v:
            v = v2
            move = a

    return v, move

def minValue(state):
    player = movesNext(state)
    if player == 'x':
        state.turn = 'o'
    elif player == 'o':
        state.turn = 'x'
    
    if isTerminal(state):
        util = utility(state,initialPlayer)
        
        return util, None
    
    v = float('inf')

    for a in actions(state):
        global count
        count = count + 1
        thetuple = maxValue(result(state,a))
        
        v2 = thetuple[0]
        a2 = thetuple[1]
        
        if v2 < v:
            v = v2
            move = a

    return v, move

def alphaBetaSearch(state):
    player = movesNext(state) #Initial player is set
  
    valMoveTuple = alphaBetaMinVal(state,float('-inf'),float('inf'))
    value = valMoveTuple[0] #Utility from minValue is stored here
    move = valMoveTuple[1] #Move from minValue is stored here
    return move

def alphaBetaSearch2(state):
    #This function is for computer 2 in computer vs computer
    player = movesNext(state) #Initial player is set
  
    valMoveTuple = alphaBetaMaxVal(state,float('-inf'),float('inf'))
    value = valMoveTuple[0] #Utility from minValue is stored here
    move = valMoveTuple[1] #Move from minValue is stored here
    return move

def alphaBetaMinVal(state,alpha,beta):
    player = movesNext(state)
    if player == 'x':
        state.turn = 'o'
    elif player == 'o':
        state.turn = 'x'
    
    if isTerminal(state):
        util = utility(state,initialPlayer)
        
        return util, None
    
    v = float('inf')

    for a in actions(state):
        global count
        count = count + 1
        thetuple = alphaBetaMaxVal(result(state,a),alpha,beta)
        
        v2 = thetuple[0]
        a2 = thetuple[1]
        
        if v2 < v:
            v = v2
            move = a
            beta = min(beta,v)
        if v <= alpha:
            return v,move

    return v, move

def alphaBetaMaxVal(state,alpha,beta):
    player = movesNext(state)
    if player == 'x':
        state.turn = 'o'
    elif player == 'o':
        state.turn = 'x'
    
    if isTerminal(state):
        util = utility(state,initialPlayer)
        
        return util, None
    
    v = float('-inf')

    for a in actions(state):
        global count
        count = count + 1
        thetuple = alphaBetaMinVal(result(state,a),alpha,beta)
        
        v2 = thetuple[0]
        a2 = thetuple[1]
        
        if v2 > v:
            v = v2
            move = a
            alpha = max(alpha,v)
        if v >= beta:
            return v,move

    return v, move

initBoard = State([None,None,None,None,None,None,None,None,None],initialPlayer) #Initializing the empty board

print("Soylu, Rana, A20465152 solution:")
if sys.argv[1] == '1':
    print("Algorithm: MiniMax")
elif sys.argv[1] == '2':
    print("Algorithm: MiniMax with alpha-beta pruning")
print("First:", initialPlayer, )
if sys.argv[3] == '1':
    print("Mode: human versus player")
elif sys.argv[3] == '2':
    print("Mode: computer versus computer")

if sys.argv[1] == '1':
    #Play minimax:
    if sys.argv[3] == '1':
        #Playing human vs computer
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        
        currentState = initBoard
        while isTerminal(currentState) == False:
            #It is the player's turn
            #Ask player their input. Take input and see if it is in current possible actions
            #After taking input, Do player's move on board. Print board.Run computer's response with the generated new board.

            print(initialPlayer,"’s move. What is your move (possible moves at the moment are:", actions(currentState)," | enter 0 to exit the game)?")
            playerInput = input()
            possibleActions = list(map(str,actions(currentState))) #maps the list to a string in order to compare with player input
            inActions = False
            isZero = False
            if playerInput in possibleActions:
                inActions = True
            
            if playerInput == '0':
                isZero = True
            while inActions == False and isZero == False: 
                print(initialPlayer,"’s move. What is your move (possible moves at the moment are:", actions(currentState)," | enter 0 to exit the game)?")
                playerInput = input()
                if playerInput in possibleActions:
                    inActions = True 
                    isZero = True #This may not actually be true but whatever i just need it to exit the loop
                if playerInput == '0':
                    inActions = True 
                    isZero = True

            if playerInput == '0':
                exit()
            #Create the resulting board in the system.
            if playerInput in possibleActions:
                currentState = result(currentState,int(playerInput))

            #Printing board
            if currentState.board[0] == None:
                one = ' '
            else:
                one = currentState.board[0]
            if currentState.board[1] == None:
                two = ' '
            else:
                two = currentState.board[1]
            if currentState.board[2] == None:
                three = ' '
            else:
                three = currentState.board[2]
            if currentState.board[3] == None:
                four = ' '
            else:
                four = currentState.board[3]
            if currentState.board[4] == None:
                five = ' '
            else:
                five = currentState.board[4]
            if currentState.board[5] == None:
                six = ' '
            else:
                six = currentState.board[5]
            if currentState.board[6] == None:
                seven = ' '
            else:
                seven = currentState.board[6]
            if currentState.board[7] == None:
                eight = ' '
            else:
                eight = currentState.board[7]
            if currentState.board[8] == None:
                nine = ' '
            else:
                nine = currentState.board[8]
            
            

            print(" ",one," | ",two," | ",three," ")
            print("-----+-----+-----")
            print(" ",four," | ",five," | ",six," ")
            print("-----+-----+-----")
            print(" ",seven," | ",eight," | ",nine," ") 


            #Computer's turn
            #Check if terminal state
            if isTerminal(currentState) == False:
                #Computer will run minimax algorithm on current board to find next move
                if initialPlayer == 'x':
                    computerSide = 'o'
                elif initialPlayer == 'o':
                    computerSide = 'x'
                
                count = 1
                computerMove = minimaxSearch(currentState)
                print(computerSide,"’s selected move:",computerMove, ". Number of search tree nodes generated:",count)

                currentState = result(currentState,computerMove)
                

                #Print current board again

                if currentState.board[0] == None:
                    one = ' '
                else:
                    one = currentState.board[0]
                if currentState.board[1] == None:
                    two = ' '
                else:
                    two = currentState.board[1]
                if currentState.board[2] == None:
                    three = ' '
                else:
                    three = currentState.board[2]
                if currentState.board[3] == None:
                    four = ' '
                else:
                    four = currentState.board[3]
                if currentState.board[4] == None:
                    five = ' '
                else:
                    five = currentState.board[4]
                if currentState.board[5] == None:
                    six = ' '
                else:
                    six = currentState.board[5]
                if currentState.board[6] == None:
                    seven = ' '
                else:
                    seven = currentState.board[6]
                if currentState.board[7] == None:
                    eight = ' '
                else:
                    eight = currentState.board[7]
                if currentState.board[8] == None:
                    nine = ' '
                else:
                    nine = currentState.board[8]
                
                

                print(" ",one," | ",two," | ",three," ")
                print("-----+-----+-----")
                print(" ",four," | ",five," | ",six," ")
                print("-----+-----+-----")
                print(" ",seven," | ",eight," | ",nine," ") 

                #Change turn back to player's turn
                
                currentPlayer = currentState.turn 
                if currentPlayer == 'x':
                    currentState.turn = 'o'
                elif currentPlayer == 'o':
                    currentState.turn = 'x'
                else:
                    print("What happened here?")
            #Game has ended in some form
            #Calculate utility
            if isTerminal(currentState) == True:
                finalResult = utility(currentState,initialPlayer)
                
                if finalResult == 1 and initialPlayer == 'x':
                    print("X WON")
                elif finalResult == 1 and initialPlayer == 'o':
                    print("O WON")
                elif finalResult == -1 and initialPlayer == 'x':
                    print("X LOST")
                elif finalResult == -1 and initialPlayer == 'o':
                    print("O LOST")
                elif finalResult == 0:
                    print("TIE")
    elif sys.argv[3] == '2':
        #Playing computer vs computer
        currentState = initBoard
        while isTerminal(currentState) == False:
                #Assigning sides to the players
                if initialPlayer == 'x':
                    computer1 = 'o'
                    computer2 = 'x'
                elif initialPlayer == 'o':
                    computer1 = 'x'
                    computer2 = 'o'
                
                count = 1
                #Computer 1's turn
                computer1Move = minimaxSearch(currentState)
                print(computer1,"’s selected move:",computer1Move, ". Number of search tree nodes generated:",count)

                currentState = result(currentState,computer1Move)
                

                #Printing the board
                if currentState.board[0] == None:
                    one = ' '
                else:
                    one = currentState.board[0]
                if currentState.board[1] == None:
                    two = ' '
                else:
                    two = currentState.board[1]
                if currentState.board[2] == None:
                    three = ' '
                else:
                    three = currentState.board[2]
                if currentState.board[3] == None:
                    four = ' '
                else:
                    four = currentState.board[3]
                if currentState.board[4] == None:
                    five = ' '
                else:
                    five = currentState.board[4]
                if currentState.board[5] == None:
                    six = ' '
                else:
                    six = currentState.board[5]
                if currentState.board[6] == None:
                    seven = ' '
                else:
                    seven = currentState.board[6]
                if currentState.board[7] == None:
                    eight = ' '
                else:
                    eight = currentState.board[7]
                if currentState.board[8] == None:
                    nine = ' '
                else:
                    nine = currentState.board[8]
                
                

                print(" ",one," | ",two," | ",three," ")
                print("-----+-----+-----")
                print(" ",four," | ",five," | ",six," ")
                print("-----+-----+-----")
                print(" ",seven," | ",eight," | ",nine," ") 

                if isTerminal(currentState) == False: #Check if game has ended yet
                    #Computer 2's turn
                    count = 1
                    computer2Move = minimaxSearch2(currentState)
                    print(computer2,"’s selected move:",computer2Move, ". Number of search tree nodes generated:",count)

                    currentState = result(currentState,computer2Move)

                    #Printing board again
                    if currentState.board[0] == None:
                        one = ' '
                    else:
                        one = currentState.board[0]
                    if currentState.board[1] == None:
                        two = ' '
                    else:
                        two = currentState.board[1]
                    if currentState.board[2] == None:
                        three = ' '
                    else:
                        three = currentState.board[2]
                    if currentState.board[3] == None:
                        four = ' '
                    else:
                        four = currentState.board[3]
                    if currentState.board[4] == None:
                        five = ' '
                    else:
                        five = currentState.board[4]
                    if currentState.board[5] == None:
                        six = ' '
                    else:
                        six = currentState.board[5]
                    if currentState.board[6] == None:
                        seven = ' '
                    else:
                        seven = currentState.board[6]
                    if currentState.board[7] == None:
                        eight = ' '
                    else:
                        eight = currentState.board[7]
                    if currentState.board[8] == None:
                        nine = ' '
                    else:
                        nine = currentState.board[8]
                    
                    

                    print(" ",one," | ",two," | ",three," ")
                    print("-----+-----+-----")
                    print(" ",four," | ",five," | ",six," ")
                    print("-----+-----+-----")
                    print(" ",seven," | ",eight," | ",nine," ") 


        if isTerminal(currentState) == True:
                finalResult = utility(currentState,initialPlayer)
                
                if finalResult == 1 and initialPlayer == 'x':
                    print("X WON")
                elif finalResult == 1 and initialPlayer == 'o':
                    print("O WON")
                elif finalResult == -1 and initialPlayer == 'x':
                    print("X LOST")
                elif finalResult == -1 and initialPlayer == 'o':
                    print("O LOST")
                elif finalResult == 0:
                    print("TIE")

elif sys.argv[1] == '2':
    #Play minimax with alpha beta search
    if sys.argv[3] == '1':
        #Playing human vs computer
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        print("-----+-----+-----")
        print("     |     |     ")
        
        currentState = initBoard
        while isTerminal(currentState) == False:
            #It is the player's turn
            #Ask player their input. Take input and see if it is in current possible actions
            #After taking input, Do player's move on board. Print board.Run computer's response with the generated new board.

            print(initialPlayer,"’s move. What is your move (possible moves at the moment are:", actions(currentState)," | enter 0 to exit the game)?")
            playerInput = input()
            possibleActions = list(map(str,actions(currentState))) #maps the list to a string in order to compare with player input

            while playerInput not in possibleActions and not '0': 
                print(initialPlayer,"’s move. What is your move (possible moves at the moment are:", actions(currentState)," | enter 0 to exit the game)?")
                playerInput = input()
            if playerInput == '0':
                exit()
            #Create the resulting board in the system.
            if playerInput in possibleActions:
                currentState = result(currentState,int(playerInput))

            #Printing board
            if currentState.board[0] == None:
                one = ' '
            else:
                one = currentState.board[0]
            if currentState.board[1] == None:
                two = ' '
            else:
                two = currentState.board[1]
            if currentState.board[2] == None:
                three = ' '
            else:
                three = currentState.board[2]
            if currentState.board[3] == None:
                four = ' '
            else:
                four = currentState.board[3]
            if currentState.board[4] == None:
                five = ' '
            else:
                five = currentState.board[4]
            if currentState.board[5] == None:
                six = ' '
            else:
                six = currentState.board[5]
            if currentState.board[6] == None:
                seven = ' '
            else:
                seven = currentState.board[6]
            if currentState.board[7] == None:
                eight = ' '
            else:
                eight = currentState.board[7]
            if currentState.board[8] == None:
                nine = ' '
            else:
                nine = currentState.board[8]
            
            

            print(" ",one," | ",two," | ",three," ")
            print("-----+-----+-----")
            print(" ",four," | ",five," | ",six," ")
            print("-----+-----+-----")
            print(" ",seven," | ",eight," | ",nine," ") 


            #Computer's turn
            #Check if terminal state
            if isTerminal(currentState) == False:
                #Computer will run minimax algorithm on current board to find next move
                if initialPlayer == 'x':
                    computerSide = 'o'
                elif initialPlayer == 'o':
                    computerSide = 'x'
                
                count = 1
                computerMove = alphaBetaSearch(currentState)
                print(computerSide,"’s selected move:",computerMove, ". Number of search tree nodes generated:",count)

                currentState = result(currentState,computerMove)
                

                #Print current board again

                if currentState.board[0] == None:
                    one = ' '
                else:
                    one = currentState.board[0]
                if currentState.board[1] == None:
                    two = ' '
                else:
                    two = currentState.board[1]
                if currentState.board[2] == None:
                    three = ' '
                else:
                    three = currentState.board[2]
                if currentState.board[3] == None:
                    four = ' '
                else:
                    four = currentState.board[3]
                if currentState.board[4] == None:
                    five = ' '
                else:
                    five = currentState.board[4]
                if currentState.board[5] == None:
                    six = ' '
                else:
                    six = currentState.board[5]
                if currentState.board[6] == None:
                    seven = ' '
                else:
                    seven = currentState.board[6]
                if currentState.board[7] == None:
                    eight = ' '
                else:
                    eight = currentState.board[7]
                if currentState.board[8] == None:
                    nine = ' '
                else:
                    nine = currentState.board[8]
                
                

                print(" ",one," | ",two," | ",three," ")
                print("-----+-----+-----")
                print(" ",four," | ",five," | ",six," ")
                print("-----+-----+-----")
                print(" ",seven," | ",eight," | ",nine," ") 

                #Change turn back to player's turn
                
                currentPlayer = currentState.turn 
                if currentPlayer == 'x':
                    currentState.turn = 'o'
                elif currentPlayer == 'o':
                    currentState.turn = 'x'
                else:
                    print("What happened here?")
            #Game has ended in some form
            #Calculate utility
            if isTerminal(currentState) == True:
                finalResult = utility(currentState,initialPlayer)
                
                if finalResult == 1 and initialPlayer == 'x':
                    print("X WON")
                elif finalResult == 1 and initialPlayer == 'o':
                    print("O WON")
                elif finalResult == -1 and initialPlayer == 'x':
                    print("X LOST")
                elif finalResult == -1 and initialPlayer == 'o':
                    print("O LOST")
                elif finalResult == 0:
                    print("TIE")
    elif sys.argv[3] == '2':
        #Playing computer vs computer
        currentState = initBoard
        while isTerminal(currentState) == False:
                #Assigning sides to the players
                if initialPlayer == 'x':
                    computer1 = 'o'
                    computer2 = 'x'
                elif initialPlayer == 'o':
                    computer1 = 'x'
                    computer2 = 'o'
                
                count = 1
                #Computer 1's turn
                computer1Move = alphaBetaSearch(currentState)
                print(computer1,"’s selected move:",computer1Move, ". Number of search tree nodes generated:",count)

                currentState = result(currentState,computer1Move)
                

                #Printing the board
                if currentState.board[0] == None:
                    one = ' '
                else:
                    one = currentState.board[0]
                if currentState.board[1] == None:
                    two = ' '
                else:
                    two = currentState.board[1]
                if currentState.board[2] == None:
                    three = ' '
                else:
                    three = currentState.board[2]
                if currentState.board[3] == None:
                    four = ' '
                else:
                    four = currentState.board[3]
                if currentState.board[4] == None:
                    five = ' '
                else:
                    five = currentState.board[4]
                if currentState.board[5] == None:
                    six = ' '
                else:
                    six = currentState.board[5]
                if currentState.board[6] == None:
                    seven = ' '
                else:
                    seven = currentState.board[6]
                if currentState.board[7] == None:
                    eight = ' '
                else:
                    eight = currentState.board[7]
                if currentState.board[8] == None:
                    nine = ' '
                else:
                    nine = currentState.board[8]
                
                

                print(" ",one," | ",two," | ",three," ")
                print("-----+-----+-----")
                print(" ",four," | ",five," | ",six," ")
                print("-----+-----+-----")
                print(" ",seven," | ",eight," | ",nine," ") 

                if isTerminal(currentState) == False: #Check if game has ended yet
                    #Computer 2's turn
                    count = 1
                    computer2Move = alphaBetaSearch2(currentState)
                    print(computer2,"’s selected move:",computer2Move, ". Number of search tree nodes generated:",count)

                    currentState = result(currentState,computer2Move)

                    #Printing board again
                    if currentState.board[0] == None:
                        one = ' '
                    else:
                        one = currentState.board[0]
                    if currentState.board[1] == None:
                        two = ' '
                    else:
                        two = currentState.board[1]
                    if currentState.board[2] == None:
                        three = ' '
                    else:
                        three = currentState.board[2]
                    if currentState.board[3] == None:
                        four = ' '
                    else:
                        four = currentState.board[3]
                    if currentState.board[4] == None:
                        five = ' '
                    else:
                        five = currentState.board[4]
                    if currentState.board[5] == None:
                        six = ' '
                    else:
                        six = currentState.board[5]
                    if currentState.board[6] == None:
                        seven = ' '
                    else:
                        seven = currentState.board[6]
                    if currentState.board[7] == None:
                        eight = ' '
                    else:
                        eight = currentState.board[7]
                    if currentState.board[8] == None:
                        nine = ' '
                    else:
                        nine = currentState.board[8]
                    
                    

                    print(" ",one," | ",two," | ",three," ")
                    print("-----+-----+-----")
                    print(" ",four," | ",five," | ",six," ")
                    print("-----+-----+-----")
                    print(" ",seven," | ",eight," | ",nine," ") 


        if isTerminal(currentState) == True:
                finalResult = utility(currentState,initialPlayer)
                
                if finalResult == 1 and initialPlayer == 'x':
                    print("X WON")
                elif finalResult == 1 and initialPlayer == 'o':
                    print("O WON")
                elif finalResult == -1 and initialPlayer == 'x':
                    print("X LOST")
                elif finalResult == -1 and initialPlayer == 'o':
                    print("O LOST")
                elif finalResult == 0:
                    print("TIE")

        


    #move 1: minimax generated= 59705 + 935 + 47 + 5 beta pruning= 2338 + 75 + 17
    #move 2 minimax = 63905 + 1055 + 51 + 5 beta pruning = 2869 + 269 + 33 + 5
    #move 3: minimax = 59705 + 935 + 47 + 5 beta pruning = 3275 + 131 + 29 + 5
    #move 4: minimax = 63905 + 1055 + 53 + 5 beta pruning = 3574 + 179 + 33 + 5
    #move 5: minimax = 55505 + 1055 + 53 + 5 beta pruning = 2316 + 179 + 33 + 5
    #move 6: minimax = 63905 + 1465 + 51 + 5 beta pruning = 3590 + 396 + 34 + 5
    #move 7: minimax = 59705 + 935 + 47 + 5 beta pruning = 3809 + 144 + 40 + 5
    #move 8 minimax = 63905 + 1585 + 53 + 5 beta pruning = 4981 + 671 + 51 + 5
    #move 9 minimax = 59705 + 1277 + 61 + 5 beta pruning = 3957 + 451 + 33 + 5

