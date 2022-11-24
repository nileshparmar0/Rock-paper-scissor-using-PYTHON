import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return'Its a tie'

    if win(user,computer):
        return'You won'

    return'You lost'

def win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent =='r') or (player == 's' and opponent == 'p'):
        return True

print(play())