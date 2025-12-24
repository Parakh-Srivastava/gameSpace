import random as ra

def initialAmountSet():
    amountSel = ra.randint(2, 6)
    InitialAmount = 10 ** (amountSel + 1)
    print("The amount you get : $", InitialAmount)
    return InitialAmount

def ContinueGambling(Amount):
    inp = input("Do you wanna play again ! [Yes || No] : ")
    inputLower = inp.lower()

    if inputLower[0] == 'y':
        casino(Amount, int(input("Enter the betting amount : $")))
    elif inputLower[0] == 'n':
        print("Exiting casino !!")
        return
    else:
        print("invalid output !!")
        ContinueGambling(Amount)

def casino(Amount, BettingAmount):
    if Amount > 0 and BettingAmount <= Amount:
        slot1 = ra.randint(1, 3)
        slot2 = ra.randint(1, 3)
        slot3 = ra.randint(1, 3)
        print(f"{slot1} | {slot2} | {slot3}")
        
        if slot1 == slot2 == slot3:
            Amount += (BettingAmount * 999)
            print("Congratulations, You get $", BettingAmount * 1000)
            print(f"You have now ${Amount}")
            ContinueGambling(Amount)
        else:
            print("you lose !!")
            Amount -= BettingAmount
            print(f"You have now ${Amount}")
            if Amount != 0:
                ContinueGambling(Amount)
            else:
                print("Now fuck off you broke ass nigga")
    elif Amount == 0:
        print("No money left to play lil bro !")
        return
    else:
        print(f"You only got ${Amount} you broke ass nigga !!")
        ContinueGambling(Amount)

class Casino():
    def main():
        InitialAmount = initialAmountSet(); 
        BettingAmount = int(input("Enter the betting amount : $"))
        casino(InitialAmount, BettingAmount)

if __name__ == "__main__":
    Casino.main()