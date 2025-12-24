import random
gameboard = [[1,'|',2,'|',3],['-','+','-','+','-'],[4,'|',5,'|',6],['-','+','-','+','-'],[7,'|',8,'|',9]]

def gb():
    for i in range(0,5):
        for j in range(0,5):
            print(gameboard[i][j], end=' ')
        print()

def inputC(XO):

    inp = random.randint(1,9)
    
    while (1 > inp) or (inp > 9):
        inp = int(input("Enter numbers from 1 to 9 buddy :")) #Value under 1 to 9 will be selected

    for i in range(0,5):
        for j in range(0,5):
            if gameboard[i][j] == inp:
                break
        if gameboard[i][j] == inp:
            break

    if gameboard[i][j] == inp:
        gameboard[i][j] = XO
        print(f"{XO} plays {inp}.")    
    else:
        inputC(XO)

def input_Value(XO):

    inp = int(input(f"{XO}'s turn :"))
    
    while (1 > inp) or (inp > 9): 
        inp = int(input("Enter numbers from 1 to 9 buddy :"))   #Value under 1 to 9 will be selected
        
    for i in range(0,5):
        for j in range(0,5):
            if gameboard[i][j] == inp :
                break
        if gameboard[i][j] == inp:
            break
        
    if gameboard[i][j] == inp:        #So that we can see if the entered number is not already filled.
        gameboard[i][j] = XO
    else:
        print("invalid output !")
        input_Value(XO)

def gameEnd(XO):
    if((gameboard[0][0] == XO and gameboard[0][2] == XO and gameboard[0][4] == XO)
       or (gameboard[2][0] == XO and gameboard[2][2] == XO and gameboard[2][4] == XO)
       or (gameboard[4][0] == XO and gameboard[4][2] == XO and gameboard[4][4] == XO)
       or (gameboard[0][0] == XO and gameboard[2][0] == XO and gameboard[4][0] == XO)
       or (gameboard[0][2] == XO and gameboard[2][2] == XO and gameboard[4][2] == XO)
       or (gameboard[0][4] == XO and gameboard[2][4] == XO and gameboard[4][4] == XO)
       or (gameboard[0][0] == XO and gameboard[2][2] == XO and gameboard[4][4] == XO) 
       or (gameboard[0][4] == XO and gameboard[2][2] == XO and gameboard[4][0] == XO)):
        print(f"{XO} wins !!")
        return True
    else:
        return False

def gameDraw():
    if(gameboard[0][0] != 1 and gameboard[0][2] != 2 and gameboard[0][4] != 3
       and gameboard[2][0] != 4 and gameboard[2][2] != 5 and gameboard[2][4] != 6
       and gameboard[4][0] != 7 and gameboard[4][2] != 8 and gameboard[4][4] != 9):
        print("The game is a draw !!")
        return True
    else:
        return False

class TicTacToe():
    
    def main():
        
        try:
            print("Write the number where you want the respective symbol !!")
            gb()
            CorP = int(input("[Enter 1 for PvP] | [Enter 2 for PvC] : "))
            if CorP == 2:
                XorO = int(input("[Enter 1 to select O] [Enter 2 to select X] : \n"))
            while True:
                
                if CorP == 1:
                    input_Value('X')
                elif CorP == 2:
                    if XorO == 1:
                        inputC('X')
                    elif XorO == 2:
                        input_Value('X')
                    else :
                        print("Either 1 or 2, game closed due to retardness.")
                        break
                else :
                    print("Either 1 or 2, game closed due to retardness.")
                    break
                print("\n")
                
                gb()
                if gameEnd('X') == True:
                    break
                elif gameDraw() == True:      
                    break
                
                if CorP == 1:
                    input_Value('O')
                elif CorP == 2:
                    if XorO == 1:
                        input_Value('O')
                    elif XorO == 2:
                        inputC('O')
                print("\n")

                gb()
                if gameEnd('O') == True:
                    break
                elif gameDraw() == True:      
                    break
        
        except ValueError:
            print("Input had to be a number\n")
        
        finally:
            playAgain = input("Do you wanna play again ! :")

            if playAgain[0] == "y" or playAgain[0] == "Y":
                gameboard[0][0] = 1
                gameboard[0][2] = 2
                gameboard[0][4] = 3
                gameboard[2][0] = 4
                gameboard[2][2] = 5
                gameboard[2][4] = 6
                gameboard[4][0] = 7
                gameboard[4][2] = 8
                gameboard[4][4] = 9
                TicTacToe.main()
            elif playAgain[0] == "n" or playAgain == "N":
                print("Exiting game !")
            else:
                print("Not a yes or a no results in the closing of the game !!")

if __name__ == "__main__":
    TicTacToe.main()