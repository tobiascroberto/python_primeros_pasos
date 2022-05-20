import random

def play():
    user = input("'r' for rock, 's' for scissors or 'p' for paper: What is your choice? ")
    computer = random.choice(['r','s','p'])

    if user == computer:
        return 'It\'s a tie.'

    if is_win(user,computer):
        return "You win"
    
    return "You lost. "

def is_win(player,computer):
    if (player == 'r' and computer =='s') or (player == 's' and computer =='p') or (player == 'p' and computer =='r'):
        return True

print(play())