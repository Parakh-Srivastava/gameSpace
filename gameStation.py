from StonePaperScissor import StonePaperScissor as SPS
from ticTacToe import TicTacToe as TTT
from casino import Casino as CAS

print("\t\t\t Welcome to game station !!!")
print("Enter the serial number of the game you want to play : \n1) Tic Tac Toe \n2)Stone Paper Scissor \n3) Casino\n\n")

while True:
    try:
        game = int(input())
        break    

    except ValueError:
        print("The entered value should be a number .")
    except Exception:
        print("Something went wrong !!")

match game:
    case 1:
        TTT.main()
    case 2:
        SPS.main(0,0)
    case 3:
        CAS.main()
    case _:
        print("Only game available are the one listed above !!")