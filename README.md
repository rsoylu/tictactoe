# Tic Tac Toe  
![image](https://github.com/rsoylu/tictactoe/assets/70935031/4495bdb5-29e9-4732-8ab4-871ea501e2cd)  
This is a tic tac toe game implemented using the above pseudocode, the minimax search algorithm.  

Additionally, I have implemented the tic tac toe game using alpha beta pruning, with the following pseudocode.  
![image](https://github.com/rsoylu/tictactoe/assets/70935031/1e91bd60-03aa-4bb2-8763-1e1440a643b6)

# How it works

To run the program, you must use the command line. The program accepts 3 command line arguments, so the code can be executed with  
python cs480_P01_AXXXXXXXX.py ALGO FIRST MODE  
where:  
■ cs480_P01_AXXXXXXXX.py is your python code file name,  
■ ALGO specifies which algorithm the computer player will use:  
◆ 1 – MiniMax,  
◆ 2 – MiniMax with alpha-beta pruning,  
■ FIRST specifies who begins the game:  
◆ X  
◆ O  
■ MODE is mode in which your program should operate:  
◆ 1 – human (X) versus computer (O),  
◆ 2 – computer (X) versus computer (O)  

Example:  
python cs480_P01_A11111111.py 2 X 1  

The above command will run the program with the minimax alpha beta pruning algorithm where the player who begins the game is X and the mode is human versus computer.

If the number of arguments provided is NOT three (none, one, two or more than three) or arguments are invalid (incorrect ALGO, FIRST or MODE) the program displays the following error:
ERROR: Not enough/too many/illegal input arguments.
and exits.

# Program Details  
■ The Tic-Tac-Toe game board is represented by 3 x 3 grid with cells numbered as follows  
![image](https://github.com/rsoylu/tictactoe/assets/70935031/5a4d3735-9fa3-4cad-83bb-4956b12dc3fe)  

■ Possible moves/actions for both players match cell numbers (if a player wants to place an ‘X’ in the middle of the board, the move/action is ‘5’,  

# Example Game  
![image](https://github.com/rsoylu/tictactoe/assets/70935031/c0786236-6336-4ce6-9fe0-c5b4be2f0d86)  
![image](https://github.com/rsoylu/tictactoe/assets/70935031/271922c5-a68a-4a47-9631-d6227d0cd993)




