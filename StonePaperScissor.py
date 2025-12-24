import random as ra

Elements = ["Stone", "Paper", "Scissor"]
PElements = ['St', 'Pa', 'Sc']
CompPoint = 0
PlayerPoint = 0

def Inp():

    ComputerInput = Elements[ra.randint(0,2)]
    TempPlayer = input("Player plays ------->")
    PlayerInput = TempPlayer[0].capitalize() + TempPlayer[1].lower()
    return ComputerInput, PlayerInput

class StonePaperScissor():
    def main(CompPoint, PlayerPoint):

        while CompPoint != 5 and PlayerPoint != 5:
            
            try:
                CI, PI = Inp()
            
                print(f"Computer plays -----> {CI}\n")

                if (CI[0].capitalize() + CI[1].lower()) == PI:
                    print("Draw Round !!")
                elif ((CI == Elements[2] and PI == PElements[1]) or (CI == Elements[1] and PI == PElements[0]) or (CI == Elements[0] and PI == PElements[2])):
                    print("Computer wins !!")
                    CompPoint += 1
                elif ((PI == PElements[2] and CI == Elements[1]) or (PI == PElements[1] and CI == Elements[0]) or (PI == PElements[0] and CI == Elements[2])):
                    print("Player wins!!")
                    PlayerPoint += 1
                else:
                    print("Wrong input !")
            except Exception:
                print("Wrong input (At least write [st,sc or pa])")
            finally:
                print(f"\nComputer's Point = {CompPoint} || Player's Points = {PlayerPoint}\n")

        if CompPoint == 5:
            print("Computer wins the game !!")
        else:
            print("Player wins the game !!")

if __name__ == "__main__":
    StonePaperScissor.main(CompPoint, PlayerPoint)