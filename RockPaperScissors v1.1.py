# This is a rock-paper-scissors game
# Notes and info in project doc and in RPS Archive folder

import random

rockWin=('Rock wins')
rockLoss=('Rock loses')
scissorWin=('Scissors wins')
scissorLoss=('Scissors loses')
paperWin=('Paper wins')
paperLoss=('Paper loses')
Tie=('Tie')

options=('r', 'p', 's') # tuple to store options
resp=random.choice(options) # resp is computer

print("Enter one of the following options: \nr for rock \np for paper \ns for scissors \n")
userChoice=input('Enter your choice:')

print("The computer has chosen -> ", resp,)
    
# COMBINATIONS - OUTPUT
if resp == 'p' and userChoice == 'r':
    print(rockLoss, ' - The COMPUTER has WON over Rock.')

elif resp == 'r' and userChoice == 'p':
    print(paperWin, ' - The USER has WON over Rock.')

elif resp == 'r' and userChoice == 'r':
    print(Tie, ' - Rock and Rock.')

elif resp == 's' and userChoice == 'p':
    print(scissorWin, ' - The COMPUTER has WON over Paper.')

elif resp == 'p' and userChoice == 's':
    print(scissorWin, ' - The USER has WON over Paper.')

elif resp == 'p' and userChoice == 'p':
    print(Tie, ' - Paper and Paper.')

elif resp == 'r' and userChoice == 's':
    print(rockWin, ' - The COMPUTER has WON over Scissors.')
    
elif resp == 's' and userChoice == 'r':
    print(rockWin, ' - The USER has WON over Scissors.') 

elif resp == 's' and userChoice == 's':
    print(Tie, ' Scissors and Scissors.')

